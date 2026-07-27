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

machine_on = True

while machine_on == True:
    print ("Welcome to Gold's Coffee Machine, please check our menu: Espresso: 1.50$, Latte:2.50$, Cappucino: 3.00$ ")
    coffee_order = input ("What would you like? Espresso, Latte, Cappucino ").lower()

    #Off Button
    if coffee_order == 'off':
        machine_on = False

    if coffee_order == 'report': 
        print (f"Water: {water} ml")
        print (f"Milk: {milk} ml")
        print (f"Coffe: {coffee} mg")
        print (f"Money: {money} $")

    if coffee_order == 'espresso': 
        quarter_input = int (input ("Please insert quarters "))
        dime_input = int (input ("Please insert dime "))
        nickel_input = int (input ("Please insert nickels "))
        penny_input = int (input ("Please insert pennies "))

        payment_calc = (quarter * quarter_input) + (dime * dime_input) + (nickel * nickel_input) + (pennies * penny_input)
        espresso_price = float (1.50)
        change = payment_calc - espresso_price
        
        if payment_calc > espresso_price:
            if water < 50 or coffee < 18: 
                print ("Not enough resources! Can't make your coffee buddy. Money refunded. ")
            elif water > 50 and coffee > 18:    
                print ("Here is your espresso!")
                print (f"Here is your change {change:.2f} cents")
                water -= 50
                coffee -= 18
                money += 1.50
        elif payment_calc < espresso_price: 
            print ("Sorry that's not enough money. Money refunded.")        

    if coffee_order == 'latte': 
        quarter_input = int (input ("Please insert quarters "))
        dime_input = int (input ("Please insert dime "))
        nickel_input = int (input ("Please insert nickels "))
        penny_input = int (input ("Please insert pennies "))

        payment_calc = (quarter * quarter_input) + (dime * dime_input) + (nickel * nickel_input) + (pennies * penny_input)
        latte_price = float (2.50)
        change = payment_calc - latte_price
        
        if payment_calc > latte_price:
            if water < 200 or coffee < 24 or milk < 150: 
                print ("Not enough resources! Can't make your coffee buddy. Money refunded. ")
            elif water > 50 and coffee > 18 and milk > 150:    
                print ("Here is your latte!")
                print (f"Here is your change {change:.2f} cents")
                water -= 200
                coffee -= 24
                milk -= 150
                money += 2.50
        elif payment_calc < latte_price: 
            print ("Sorry that's not enough money. Money refunded.") 

    if coffee_order == 'cappucino': 
        quarter_input = int (input ("Please insert quarters "))
        dime_input = int (input ("Please insert dime "))
        nickel_input = int (input ("Please insert nickels "))
        penny_input = int (input ("Please insert pennies "))

        payment_calc = (quarter * quarter_input) + (dime * dime_input) + (nickel * nickel_input) + (pennies * penny_input)
        cappucino_price = float (3.00)
        change = payment_calc - cappucino_price
        
        if payment_calc > cappucino_price:
            if water < 250 or coffee < 24 or milk < 100: 
                print ("Not enough resources! Can't make your coffee buddy. Money refunded. ")
            elif water > 250 and coffee > 24 and milk > 100:    
                print ("Here is your Cappucino!")
                print (f"Here is your change {change:.2f} cents")
                water -= 250
                coffee -= 24
                milk -= 100
                money += 3.00
        elif payment_calc < cappucino_price: 
            print ("Sorry that's not enough money. Money refunded.") 