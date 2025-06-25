class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

class Main:
    def run(self):
        calc = Calculator()
        while True:
            print("\nCalculator Menu:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")
            choice = input("Choose an operation (1-5): ")
            if choice == '5':
                print("Exiting calculator.")
                break
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Try again.")
                continue
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if choice == '1':
                    result = calc.add(a, b)
                elif choice == '2':
                    result = calc.subtract(a, b)
                elif choice == '3':
                    result = calc.multiply(a, b)
                elif choice == '4':
                    result = calc.divide(a, b)
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    Main().run()
