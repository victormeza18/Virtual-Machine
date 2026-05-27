# --- Implementación Única del Autómata Finito---

class Pattern:
    def __init__(self, p: str):
        self._pattern = p

    def set_pattern(self, p: str):
        self._pattern = p

    def get_pattern(self) -> str:
        return self._pattern

class RegularExpression:
    def __init__(self, p: Pattern):
        self.pattern = p

    def is_valid(self, input_str: str) -> bool:
        raise NotImplementedError

    def is_accepted_symbol(self, symbol: str) -> bool:
        raise NotImplementedError

class AlphabeticExpression(RegularExpression):
    def is_valid(self, input_str: str) -> bool:
        if not input_str:
            return False
        return all(c.isalpha() for c in input_str)

    def is_accepted_symbol(self, symbol: str) -> bool:
        return symbol.isalpha()

class NumericExpression(RegularExpression):
    def is_valid(self, input_str: str) -> bool:
        if not input_str:
            return False
        return all(c.isdigit() for c in input_str)

    def is_accepted_symbol(self, symbol: str) -> bool:
        return symbol.isdigit()

class FiniteStateAutomata:
    def __init__(self, expr: RegularExpression):
        self.initial_state = 0
        self.accept_state = 1
        self.current_state = self.initial_state
        self.expression = expr

    def reset(self):
        self.current_state = self.initial_state

    def transition(self, symbol: str) -> bool:
        if self.current_state == 0:
            if self.expression.is_accepted_symbol(symbol):
                self.current_state = 1
                return True
            return False
        elif self.current_state == 1:
            if self.expression.is_accepted_symbol(symbol):
                self.current_state = 1
                return True
            return False
        return False

    def process(self, input_str: str) -> bool:
        self.reset()
        if not input_str:
            return False
        for char in input_str:
            if not self.transition(char):
                return False
        return self.is_accepting_state() and self.expression.is_valid(input_str)

    def is_accepting_state(self) -> bool:
        return self.current_state == self.accept_state

    def get_current_state(self) -> int:
        return self.current_state

def main():
    option = 0
    while option != 3:
        print("\n" + "="*42)
        print(" Deterministic Finite State Automata (FSA)")
        print(" 1. Validate alphabetic string [A-Za-z]+")
        print(" 2. Validate numeric string [0-9]+")
        print(" 3. Exit")
        print("="*42)
        
        try:
            line = input("Choose an option: ")
            if not line: continue
            option = int(line)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            pattern = Pattern("[A-Za-z]+")
            expression = AlphabeticExpression(pattern)
            automata = FiniteStateAutomata(expression)
            user_input = input("Enter an alphabetic string: ")
            
            if automata.process(user_input):
                print("Result: ACCEPTED")
            else:
                print("Result: REJECTED")
            print(f"Final state: q{automata.get_current_state()}")

        elif option == 2:
            pattern = Pattern("[0-9]+")
            expression = NumericExpression(pattern)
            automata = FiniteStateAutomata(expression)
            user_input = input("Enter a numeric string: ")
            
            if automata.process(user_input):
                print("Result: ACCEPTED")
            else:
                print("Result: REJECTED")
            print(f"Final state: q{automata.get_current_state()}")

        elif option != 3:
            print("Invalid option.")

    print("Program finished.")

if __name__ == "__main__":
    main()