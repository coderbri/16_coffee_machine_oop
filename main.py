from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# * Object Instantiation
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_coffee_machine_on = True

# * Coffee Machine Simulation
while is_coffee_machine_on:
    options = menu.get_items()
    
    choice = input(f"What would you like? ({options}): ")
    
    if choice == "off":
        is_coffee_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)     # ex: latte
        # print(drink)                      # ex: <menu.MenuItem object at 0x100bfae50>
        # print(coffee_maker.is_resource_sufficient(drink))   # ex: True
        if coffee_maker.is_resource_sufficient(drink):
            # print(money_machine.make_payment(drink.cost))
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
