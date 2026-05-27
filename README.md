# Deterministic Finite State Automata (FSA) - Python

**Alumnos:**
* Ávila Ochoa Diego Josué
* Meza Díaz Víctor Uriel

---

Este proyecto es una implementación de un Autómata Finito Determinista (DFA) capaz de validar cadenas de texto según reglas específicas (alfabéticas o numéricas). El código ha sido consolidado en un único archivo para facilitar su ejecución y estudio.

## 📄 Descripción

---

El programa permite al usuario interactuar con un menú para validar si una entrada pertenece a un lenguaje regular específico:

* **Validación Alfabética:** Acepta cadenas que contienen únicamente letras `[A-Za-z]+`.
* **Validación Numérica:** Acepta cadenas que contienen únicamente dígitos `[0-9]+`.

## 🚀 Estructura del Código

---

Toda la lógica se encuentra en el archivo principal e incluye las siguientes clases:

* **Pattern:** Almacena la expresión o patrón a validar.
* **RegularExpression:** Clase base para las reglas de validación.
* **AlphabeticExpression / NumericExpression:** Implementan la lógica específica para letras y números.
* **FiniteStateAutomata:** El motor del autómata que gestiona los estados (q0 como inicial y q1 como aceptación) y las transiciones.

<br>

# Simulación de Máquina Virtual (VM)

---

Este programa es una implementación educativa de una Máquina Virtual basada en una arquitectura de registros y memoria principal. El sistema emula el comportamiento de un microprocesador ejecutando un conjunto de instrucciones mediante el Ciclo Máquina (Fetch-Decode-Execute).

### Componentes Principales

* **Unidad de Control (Control Unit):** Se encarga de la gestión lógica. Incluye un Analizador Léxico basado en autómatas para validar TOKENS PERMITIDOS (palabras reservadas, registros y dígitos) antes de su ejecución.
* **Conjunto de Instrucciones (ISA):** Soporta operaciones fundamentales como `START`, `STOP`, `MOVE` (transferencia), `ADD` (aritmética) y `STO` (almacenamiento).
* **Gestión de Registros:** Incluye registros de propósito general (`AL`, `AH`, `BL`, `BH`) y de propósito específico necesarios para el ciclo de instrucción (`PC`, `IR`, `ACC`, `MAR`, `MBR`).
* **Memoria Principal:** Simulación de un espacio de direccionamiento donde se carga el programa y se almacenan datos.

### El Ciclo Máquina

El programa procesa las instrucciones siguiendo tres estados estrictos que se imprimen en consola en tiempo real:

1. **Fetch (Búsqueda):** Se obtiene la instrucción de la memoria apuntada por el `PC` y se coloca en el `IR` a través del `MAR` y `MBR`.
2. **Decode (Decodificación):** La Unidad de Control descompone la instrucción, valida los tokens mediante autómatas y prepara los operandos.
3. **Execute (Ejecución):** Se realiza la acción física (suma, movimiento de datos o fin del programa) y se actualiza el estado de los registros y el acumulador (`ACC`).

### Salida de Datos

Al ejecutarse, el sistema muestra:

* El estado actual de todos los registros en cada fase del ciclo.
* Los resultados de las operaciones aritméticas codificadas.
* Mensajes de confirmación del cargador de programas y finalización del proceso.
