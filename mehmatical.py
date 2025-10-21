
def add(a, b):
    return (a + b)
def subtract(a, b):
    return (a - b)
def div(a, b):
    if b == "0":
        print("Well I would figure that anyone knows you cant divide by 0.")
        exit
    else :
        return (a / b)
def mult(a, b):
    return (a * b)

def main():
    print("Ugh, I guess we're doing math. Welcome to the Meh-culator.")

    a = float(input(f"Enter the first number: "))
    b = float(input(f"Enter the second number: "))
    eq = input(f"What do you want to do? (+, -, *, /): ")


    if eq == "+":
        answeradd = add()
        print(f"Fine. The answer is {answeradd} Are we done now?")
        exit


    elif eq == "-":
        answersub = subtract()
        print(f"Fine. The answer is {answersub} Are we done now?")
        exit


    elif eq == "*":
        answermult = mult()
        print(f"Fine. The answer is {answermult} Are we done now?")
        exit


    elif eq == "/": 
        answerdiv = div()
        print(f"Fine. The answer is {answerdiv} Are we done now?")
        exit
    else:
        print("You did not pick one of the equations. Cmon.")
        exit


if __name__ == "__main__":
    main()