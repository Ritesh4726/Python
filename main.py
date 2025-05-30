# main.py
# Simple calculator program

def add(a, b):
    return a + b

def main():
    print("Welcome to Simple Calculator")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = add(num1, num2)
    print("Result:", result)

if __name__ == "__main__":
    main()
