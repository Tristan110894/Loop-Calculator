"""
Filename: conditional_calculator.py
Author: <Lastname, Firstname>
Created: <MM/DD/YYYY>
Instructor: Holtslander
"""
def factorial():
    print("This program provides the functionality of a four-function calculator.\n"
        "The program will take two user-generated numbers and one of the four basic arithmetic operations\n"
        "(addition, subtraction, multiplication, and division), then perform the desired operation on the\n"
        "two numbers.\n")

    num1 = int(input("Please enter your first number on the line below.\n"))

    op = input("Please enter your desired operation.\n"
            "For addition please input: +\n"
            "For subtraction please input: -\n"
            "For multiplication please input: *\n"
            "For division please input: /\n")

    num2 = int(input("Please enter your second number on the line below.\n"))

    if op == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op == "*":
        product = 0
        for i in range(0,num2,1):
            product = product + num1
        print("The answer to your Calculation is:\n")
        print(f"{num1} * {num2} = {product}")
    elif op == "/":
        Quotient = 0
        R = num1
        while R >= num2:
            R = R - num2
            Quotient =  Quotient + 1
        
        print (f"{num1} / {num2} = {Quotient}")



        
        
    else:
        print(f"Operation: {op} is not supported.")

    print(f"\nThank you for using the four-function calculator.\n")
def main():
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this loop calculator!")

if __name__ == "__main__":
    main()