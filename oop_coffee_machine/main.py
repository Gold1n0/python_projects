from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

menu_items = menu.get_items()
print(f"Welcome to Gold's Coffee Machine please choose from the menu: {menu_items}")
machine_on = True

while machine_on == True:
    options = menu.get_items()
    choice = input (f"What would you like? {options}")
    if choice == "off": 
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)