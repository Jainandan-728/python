class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b



if __name__ == "__main__":
    calc = Calculator()

    print("10 + 5 =", calc.add(10, 5))
    print("10 - 5 =", calc.subtract(10, 5))
