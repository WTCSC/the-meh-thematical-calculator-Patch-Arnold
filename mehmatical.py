print("Ugh, I guess we're doing math. Welcome to the Meh-culator.")
a = float(input(f"Enter the first number"))
b = float(input(f"Enter the second number"))
eq = input(f"What do you want to do? (+, -, *, /)")
if eq == "+":
    def add():
        return (a + b)
    answeradd = add()
    print(f"Fine. The answer is {answeradd} Are we done now?")
    exit
elif eq == "-":
    def subtract():
        return (a - b)
    answersub = subtract()
    print(f"Fine. The answer is {answersub} Are we done now?")
    exit
elif eq == "*":
    def mult():
        return (a * b)
    answermult = mult()
    print(f"Fine. The answer is {answermult} Are we done now?")
    exit
elif eq == "/":
    def div():
        if b == "0":
            print("Well I would figure that anyone knows you cant divide by 0.")
            exit
        else :
            return (a / b)
    answerdiv = div()
    print(f"Fine. The answer is {answerdiv} Are we done now?")
    exit
else:
    print("You did not pick one of the equations. Cmon.")
    exit



