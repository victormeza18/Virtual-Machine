# --- Implementación de Máquina Virtual con Unidad de Control y Autómatas 
#     Con esto se completa la simulacion del ciclo maquina---

class Instruction:
    """Clase para modelar las instrucciones con los atributos requeridos """
    def __init__(self, name, args, interpretation, length):
        self._name = name
        self._args = args
        self._interpretation = interpretation
        self._length = length

    # Getters 
    def get_name(self): return self._name
    def get_args(self): return self._args
    def get_interpretation(self): return self._interpretation
    def get_length(self): return self._length

class LexicalAutomata:
    """Autómata para validar TOKENS PERMITIDOS (Keywords, Registros, Dígitos) """
    def __init__(self):
        self.keywords = {"START", "STOP", "MOVE", "ADD", "SUSTR", "DIV", "MULT", "STO"}
        self.registers = {"AL", "AH", "BL", "BH", "PC", "IR", "ACC", "MAR", "MBR"}

    def validate_token(self, token):
        token = token.upper()
        if token in self.keywords:
            return "KEYWORD"
        if token in self.registers:
            return "REGISTER"
        if token.isdigit():
            return "DIGIT"
        return "INVALID"

class VirtualMachine:
    def __init__(self):
        # Memoria Principal (simulada como lista)
        self.memory = [None] * 100
        
        # Registros de Propósito General y Específico 
        self.registers = {
            "PC": 0, "IR": "", "ACC": 0, "MAR": 0, "MBR": 0,
            "AL": 0, "AH": 0, "BL": 0, "BH": 0
        }
        
        self.lexer = LexicalAutomata()
        self.is_running = False

    def load_program(self, program):
        """Cargador de Programa en Memoria Principal"""
        for i, line in enumerate(program):
            self.memory[i] = line

    def print_status(self, step):
        """Imprime el estado actual del Ciclo Máquina y los Registros"""
        print(f"\n--- STATE: {step} ---")
        regs = self.registers
        print(f"PC: {regs['PC']} | IR: {regs['IR']} | ACC: {regs['ACC']}")
        print(f"MAR: {regs['MAR']} | MBR: {regs['MBR']}")
        print(f"AL: {regs['AL']} | AH: {regs['AH']} | BL: {regs['BL']} | BH: {regs['BH']}")

    def run_cycle(self):
        """Implementación del Ciclo Máquina: Fetch, Decode, Execute """
        while self.registers["PC"] < len(self.memory) and self.memory[self.registers["PC"]] is not None:
            
            # 1. FETCH: Obtener instrucción
            self.print_status("FETCH")
            self.registers["MAR"] = self.registers["PC"]
            self.registers["MBR"] = self.memory[self.registers["MAR"]]
            self.registers["IR"] = self.registers["MBR"]
            self.registers["PC"] += 1

            # 2. DECODE: Analizador Léxico (Autómata)
            self.print_status("DECODE")
            raw_instr = self.registers["IR"].replace(",", " ").split()
            tokens = []
            for t in raw_instr:
                token_type = self.lexer.validate_token(t)
                if token_type == "INVALID":
                    print(f"Error Léxico: Token '{t}' no permitido [cite: 58]")
                    return
                tokens.append(t.upper())

            # Crear objeto Instruction para la Unidad de Control 
            name = tokens[0]
            args = tokens[1:]
            instr_obj = Instruction(name, args, f"Execute {name}", len(args))

            # 3. EXECUTE: Ejecutar acción
            self.print_status("EXECUTE")
            if not self.execute(instr_obj):
                break

    def execute(self, instr):
        name = instr.get_name()
        args = instr.get_args()

        if name == "START":
            self.is_running = True
        elif name == "STOP":
            self.is_running = False
            print("\n>>> PROGRAM FINISHED")
            return False
        
        elif name == "MOVE":
            # MOVE reg, addr (mueve valor de memoria al registro)
            reg, addr = args[0], int(args[1])
            self.registers[reg] = self.memory[addr]
        
        elif name == "ADD":
            # ADD reg1, reg2
            val1 = self.registers[args[0]]
            val2 = self.registers[args[1]]
            self.registers["ACC"] = val1 + val2 # Resultado en ACC
            print(f"Arithmetic Result (ADD): {self.registers['ACC']}")

        elif name == "STO":
            # STO addr (almacena ACC en memoria)
            addr = int(args[0])
            self.memory[addr] = self.registers["ACC"]
            
        return True

# --- Ejemplo de Uso ---
if __name__ == "__main__":
    vm = VirtualMachine()

    # Datos iniciales
    vm.memory[10] = 50
    vm.memory[11] = 25

    # Instrucciones almacenadas en la memoria simulada
    test_program = [
        "START",
        "MOVE AL, 10",
        "MOVE BL, 11",
        "ADD AL, BL",
        "STO 12",
        "STOP"
    ]

    print(">>> CARGANDO PROGRAMA EN MEMORIA PRINCIPAL...")
    vm.load_program(test_program)
    
    print(">>> INICIANDO CICLO DE MÁQUINA...")
    vm.run_cycle()

    # RESUMEN EJECUTIVO
    print("\n" + "="*45)
    print("         RESUMEN DE ACCIONES FINALES")
    print("="*45)
    print(f"Operación realizada         : {test_program[3]}")
    print(f"Valor final en Acumulador   : {vm.registers['ACC']}")
    print(f"Persistencia en Memoria (12): {vm.memory[12]}")
    print(f"Estado final del PC         : {vm.registers['PC']}")
    print(f"Estado del Registro AL      : {vm.registers['AL']}")
    print(f"Estado del Registro BL      : {vm.registers['BL']}")
    print("="*45)