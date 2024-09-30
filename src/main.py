from module1 import add, subtract
from module2 import multiply, divide

def main():
    a, b = 10, 5

    print(f"Addition of {a} and {b}: {add(a, b)}")
    print(f"Subtraction of {a} and {b}: {subtract(a, b)}")
    print(f"Multiplication of {a} and {b}: {multiply(a, b)}")
    print(f"Division of {a} and {b}: {divide(a, b)}")

if __name__ == "__main__":
    main()
