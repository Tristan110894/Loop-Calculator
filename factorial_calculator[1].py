"""
Filename: factorial_calculator.py
Author: <Tristan>
Created: <3/16/2026>
Instructor: Holtslander
"""

def factorial():
    n=int( input("please enter a number for a factorial calculation\n"))
    p=1
    for i in range(n,0,-1):
        p=p*i
    print(p)

# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()
