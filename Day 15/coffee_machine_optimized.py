#value of resources
water = 2000
milk = 1500
coffee = 500
money = 0 

#value of money
quarter = float (0.25)
dime = float (0.10)
nickel = float (0.05)
pennies = float (0.01)

def collect_coins():
    quarter_input = int(input("Please insert quarters "))
    dime_input = int(input("Please insert dime "))
    nickel_input = int(input("Please insert nickels "))
    penny_input = int(input("Please insert pennies "))
    return (quarter * quarter_input) + (dime * dime_input) + (nickel * nickel_input) + (pennies * penny_input)

def make_coffee(drink_name, price, water_needed, coffee_needed, milk_needed=0):
    global water, coffee, milk, money

    payment_calc = collect_coins()
    change = payment_calc - price

    if payment_calc < price:
        print("Sorry that's not enough money. Money refunded.")
        return

    if water < water_needed or coffee < coffee_needed or milk < milk_needed:
        print("Not enough resources! Can't make your coffee buddy. Money refunded.")
        return

    print(f"Here is your {drink_name}!")
    print(f"Here is your change {change:.2f} cents")
    water -= water_needed
    coffee -= coffee_needed
    milk -= milk_needed
    money += price

machine_on = True

while machine_on == True:
    print ("Welcome to Gold's Coffee Machine, please check our menu: Espresso: 1.50$, Latte:2.50$, Cappucino: 3.00$ ")
    coffee_order = input ("What would you like? Espresso, Latte, Cappucino ").lower()

    if coffee_order == 'off':
        machine_on = False

    if coffee_order == 'report': 
        print (f"Water: {water} ml")
        print (f"Milk: {milk} ml")
        print (f"Coffe: {coffee} mg")
        print (f"Money: {money} $")

    if coffee_order == 'espresso':
        make_coffee("espresso", 1.50, 50, 18)

    if coffee_order == 'latte':
        make_coffee("latte", 2.50, 200, 24, 150)

    if coffee_order == 'cappuccino':
        make_coffee("cappuccino", 3.00, 250, 24, 100)
