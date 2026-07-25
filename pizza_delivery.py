print("Welcome to goldie's pizza!")
size = input ("What size pizza you want? S, M or L ")
meat = input ("You want extra meat on your shit? Y or N ")
cheese = input ("How about some cheese? Y or N ")

if size == "S":
    base_price = 15
elif size == "M":
    base_price = 20
elif size == "L":
    base_price = 25
else: 
    print("Get Outta Here!")

if meat == "Y": 
    if size == "S": 
        meat_bill = 2
    elif size == "M":
        meat_bill = 3
    elif size == "L":
        meat_bill = 3

if meat == "N": 
    meat_bill = 0
else: 
    print("Get outta here!")

if cheese == "Y":
    if size == "S": 
        cheese_bill = 1
    elif size == "M":
        cheese_bill = 1
    elif size == "L":
        cheese_bill = 1

if cheese == "N":
    cheese_bill = 0
else: 
    print("Get outta here!")

final_bill = base_price + meat_bill + cheese_bill

print(f"Your grand total is {final_bill}")