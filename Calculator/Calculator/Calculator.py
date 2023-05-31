def add (num1, num2): #makles the add function 
    print(num1 + num2) #prints the first number and second numbers sum
def sub (num1, num2): #makes the subtraction function
    return num1 - num2 #prints the difference of first and second number
def check_int():
    while True:
        num = input("Enter an integer: ")

        try:
           return int(num)
        except ValueError:
           print("Please enter an integer!")
def div(): #makes the division function
    num1 = check_int()
    num2 = check_int()
    return (num1/num2) #prints the quotioent of first and second number
def mult(): #makes the multiplication function
    num1 = check_int()
    num2 = check_int()
    return (num1*num2) #prints the product of first and second number
def ex(num1, num2): #makes the exponent function
    return (num1**num2) #prints the product of number one to the power of number two
def sum(numbers):
    total = 0

    for number in numbers:
        total += number
    
    return total
def main(): 
    while True:# creates infinite loop
        operation = input("what operation would you like to do? add, subraction, division, multiplication, exponent, sum, quit?").lower() #asking user what operation she'd like the calculator to do
    
        if operation == "add": #if user chooses addition
            num1 = check_int()
            num2 = check_int()
            add(num1,num2) #add two numbers together
        elif operation == "subtraction": #if operation is subraction
            num1 = check_int()
            num2 = check_int()
            print(sub(num1,num2)) #subtract two numbers
        elif operation == "division": #if operation is division
            print(div()) #divides two numbers
        elif operation == "multiplication": #if the operation is multiplication
            print(mult()) #multiplies the two numbers
        elif operation == "exponent": #if the operation is exponential
            num1 = check_int()
            num2 = check_int()
            print(ex(num1,num2)) #put number one to the power of number two
        elif operation == "sum":
            numbers = []

            while True:
                num = input("Enter stop to quit entering integers and get sum: ")

                if num == "stop":
                    break
                else:
                    num = check_int()
                    numbers.append(num)
            print(sum(numbers))
        elif operation == "quit":
            break
        else: #any other input
            print("invalid response") #tell user invalid response
    
main()

       