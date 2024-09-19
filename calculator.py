import math

class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []

    # Basic Operations
    def add(self, x, y):
        result = x + y
        self._add_to_history(f"Add: {x} + {y} = {result}")
        return result

    def subtract(self, x, y):
        result = x - y
        self._add_to_history(f"Subtract: {x} - {y} = {result}")
        return result

    def multiply(self, x, y):
        result = x * y
        self._add_to_history(f"Multiply: {x} * {y} = {result}")
        return result

    def divide(self, x, y):
        try:
            result = x / y
            self._add_to_history(f"Divide: {x} / {y} = {result}")
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    def power(self, x, y):
        result = x ** y
        self._add_to_history(f"Power: {x} ^ {y} = {result}")
        return result

    def modulus(self, x, y):
        result = x % y
        self._add_to_history(f"Modulus: {x} % {y} = {result}")
        return result

    # Advanced Operations
    def square_root(self, x):
        if x < 0:
            return "Error: Cannot compute square root of a negative number."
        result = math.sqrt(x)
        self._add_to_history(f"Square Root: sqrt({x}) = {result}")
        return result

    def factorial(self, x):
        if x < 0:
            return "Error: Factorial of a negative number is not defined."
        result = math.factorial(int(x))
        self._add_to_history(f"Factorial: {x}! = {result}")
        return result

    # Memory Functions
    def memory_add(self, value):
        self.memory += value
        return f"Memory: {self.memory}"

    def memory_subtract(self, value):
        self.memory -= value
        return f"Memory: {self.memory}"

    def memory_recall(self):
        return f"Memory Recall: {self.memory}"

    def memory_clear(self):
        self.memory = 0
        return "Memory cleared."

    # Complex Operations
    def logarithm(self, x, base=math.e):
        if x <= 0:
            return "Error: Logarithm of non-positive numbers is not defined."
        result = math.log(x, base)
        self._add_to_history(f"Logarithm: log({x}) = {result}")
        return result

    def sine(self, x):
        result = math.sin(math.radians(x))
        self._add_to_history(f"Sine: sin({x}) = {result}")
        return result

    def cosine(self, x):
        result = math.cos(math.radians(x))
        self._add_to_history(f"Cosine: cos({x}) = {result}")
        return result

    def tangent(self, x):
        try:
            result = math.tan(math.radians(x))
            self._add_to_history(f"Tangent: tan({x}) = {result}")
            return result
        except ValueError:
            return "Error: Invalid value for tangent."

    # Private helper function to track history
    def _add_to_history(self, operation):
        self.history.append(operation)

    # View the history of operations
    def view_history(self):
        if not self.history:
            return "No operations performed yet."
        return "\n".join(self.history)


def calculator():
    calc = Calculator()

    # Operation mapping for flexibility
    operations = {
        1: "Add",
        2: "Subtract",
        3: "Multiply",
        4: "Divide",
        5: "Power",
        6: "Modulus",
        7: "Square Root",
        8: "Factorial",
        9: "Logarithm",
        10: "Sine",
        11: "Cosine",
        12: "Tangent",
        13: "Memory Functions",
        14: "View History"
    }

    print("Advanced Python Calculator with Memory and History")

    while True:
        # Dynamically generate menu based on operations
        print("\nSelect an operation:")
        for number, operation in operations.items():
            print(f"{number}. {operation}")
        print(f"{len(operations) + 1}. Exit")

        try:
            choice = int(input("Enter operation number: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if choice == len(operations) + 1:
            print("Exiting the calculator. Goodbye!")
            break

        # Perform corresponding operations
        if choice in operations.keys():
            if choice in (1, 2, 3, 4, 5, 6):
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print("Error: Invalid input. Please enter numeric values.")
                    continue

                if choice == 1:
                    print(f"The result is: {calc.add(num1, num2)}")
                elif choice == 2:
                    print(f"The result is: {calc.subtract(num1, num2)}")
                elif choice == 3:
                    print(f"The result is: {calc.multiply(num1, num2)}")
                elif choice == 4:
                    print(f"The result is: {calc.divide(num1, num2)}")
                elif choice == 5:
                    print(f"The result is: {calc.power(num1, num2)}")
                elif choice == 6:
                    print(f"The result is: {calc.modulus(num1, num2)}")

            elif choice == 7:
                try:
                    num = float(input("Enter a number: "))
                except ValueError:
                    print("Error: Invalid input. Please enter a numeric value.")
                    continue
                print(f"The result is: {calc.square_root(num)}")

            elif choice == 8:
                try:
                    num = int(input("Enter a non-negative integer: "))
                except ValueError:
                    print("Error: Invalid input. Please enter an integer.")
                    continue
                print(f"The result is: {calc.factorial(num)}")

            elif choice == 9:
                try:
                    num = float(input("Enter a positive number: "))
                    base = input("Enter base (default is e): ")
                    if base:
                        base = float(base)
                        print(f"The result is: {calc.logarithm(num, base)}")
                    else:
                        print(f"The result is: {calc.logarithm(num)}")
                except ValueError:
                    print("Error: Invalid input.")
                    continue

            elif choice in (10, 11, 12):
                try:
                    angle = float(input("Enter angle in degrees: "))
                except ValueError:
                    print("Error: Invalid input. Please enter a numeric value.")
                    continue

                if choice == 10:
                    print(f"The result is: {calc.sine(angle)}")
                elif choice == 11:
                    print(f"The result is: {calc.cosine(angle)}")
                elif choice == 12:
                    print(f"The result is: {calc.tangent(angle)}")

            elif choice == 13:
                print("Memory Functions:")
                print("M+ (1): Add result to memory")
                print("M- (2): Subtract result from memory")
                print("MR (3): Recall memory")
                print("MC (4): Clear memory")
                memory_choice = input("Select memory function (1-4): ")

                if memory_choice in ('1', '2'):
                    try:
                        num = float(input("Enter the value: "))
                    except ValueError:
                        print("Error: Invalid input.")
                        continue

                    if memory_choice == '1':
                        print(calc.memory_add(num))
                    elif memory_choice == '2':
                        print(calc.memory_subtract(num))

                elif memory_choice == '3':
                    print(calc.memory_recall())
                elif memory_choice == '4':
                    print(calc.memory_clear())
                else:
                    print("Invalid choice.")

            elif choice == 14:
                print("Operation History:")
                print(calc.view_history())

        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()
