# main.py

from gcd import gcd

def main():
    print("Welcome to the GCD Calculator!")
    try:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
        result = gcd(a, b)
        print(f"The GCD of {a} and {b} is: {result}")
    except ValueError:
        print("Invalid input! Please enter integers only.")

if __name__ == "__main__":
    main()
