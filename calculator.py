class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


if __name__ == "__main__":
    calc = Calculator()

    print("Calculator Output")
    print("------------------")
    print("10 + 5 =", calc.add(10, 5))
    print("10 - 5 =", calc.subtract(10, 5))
    print("10 * 5 =", calc.multiply(10, 5))
    print("10 / 5 =", calc.divide(10, 5))
