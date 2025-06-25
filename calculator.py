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

    def square(self, a):
        return a * a

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return a ** 0.5

class Main:
    def run(self):
        calc = Calculator()
        while True:
            print("\nCalculator Menu:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Square")
            print("6. Square Root")
            print("7. Exit")
            choice = input("Choose an operation (1-7): ")
            if choice == '7':
                print("Exiting calculator.")
                break
            if choice not in ['1', '2', '3', '4', '5', '6']:
                print("Invalid choice. Try again.")
                continue
            try:
                if choice in ['1', '2', '3', '4']:
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
                elif choice == '5':
                    a = float(input("Enter a number to square: "))
                    result = calc.square(a)
                elif choice == '6':
                    a = float(input("Enter a number to square root: "))
                    result = calc.square_root(a)
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    Main().run()
