import math

print("Welcome to Gold's Simple Calculator")

def calc (n1, n2, n3):
    if n3 == "+": 
        return n1 + n2
    elif n3 == "-": 
        return n1 - n2
    elif n3 == "*": 
        return n1 * n2
    elif n3 == "/": 
        return n1 / n2


continue_calc = True

first_num = int (input("Input the first number! "))

while continue_calc == True:
    second_num = int (input("Input the next number! "))
    operator = (input ("Select your operator +, -, *, / "))

    print (f"Your results Are: {calc(first_num,second_num, operator)}")
    cont = (input ("Would you like to continue with the calculation type Y for yes and N to stop ")).lower()

    if cont == "n":
        break
    elif cont == "y": 
        first_num = calc(first_num,second_num, operator)      

