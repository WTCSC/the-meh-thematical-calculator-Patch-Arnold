#The calculator itself, is a basic calculator for everyday use. It performs additon, subtraction, multiplication and division 
#Should always return the answer within print text




#This does not use python best practices, as the rules stated we could not use the built in add, subtract, etc. functions in our code. This calculator makes the function on its own.
#This calculator is not built for values that have been squared, squarerooted, etc.






def add(a, b):
    return (a + b)
def subtract(a, b):
    return (a - b)
def div(a, b):
    if b == "0": #Checks that b is not 0, as dividing by 0 is impossible, making sure the calculator does not break
        print("Well I would figure that anyone knows you cant divide by 0.")
        exit
    else :
        return (a / b)
def mult(a, b):
    return (a * b)

def main(): #Explained along with main code at the bottom.
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

#Checks for user, and impliments the input code if there is a user detected. 
# #This is done becuase when pytest is ran it requires to not have the input
#section of the code and breaks when it does.
if __name__ == "__main__":
    main()