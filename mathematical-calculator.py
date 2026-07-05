# ====================================
# MATHEMATICAL CALCULATOR (MC)
# ====================================

print("=" * 40)
print("     MATHEMATICAL CALCULATOR")
print("=" * 40)

while True:
    print("\nOperations")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("\\  Floor Division")
    print("^  Power")
    print("%  Modulus")
    print("C  Clear")
    print("OFF Exit Calculator")

    choice = input("\nEnter Operation: ").upper()

    if choice == "OFF":
        print("Calculator Closed.")
        break

    elif choice == "C":
        print("\n" * 30)
        continue

    elif choice in ["+", "-", "*", "/", "\\", "^", "%"]:

        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == "+":
            print("Answer =", num1 + num2)

        elif choice == "-":
            print("Answer =", num1 - num2)

        elif choice == "*":
            print("Answer =", num1 * num2)

        elif choice == "/":
            if num2 == 0:
                print("Division by zero not allowed.")
            else:
                print("Answer =", num1 / num2)

        elif choice == "\\":
            if num2 == 0:
                print("Division by zero not allowed.")
            else:
                print("Answer =", num1 // num2)

        elif choice == "^":
            print("Answer =", num1 ** num2)

        elif choice == "%":
            if num2 == 0:
                print("Division by zero not allowed.")
            else:
                print("Answer =", num1 % num2)

    else:
        print("Invalid Operation!")
