from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create the objects from the blueprints
menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

turned_off = False
while not turned_off:
    prompt = input(f"What would you like? {menu.get_items()}").lower()
    item = menu.find_drink(prompt)
    if prompt == "report":
        coffe_maker.report()
        money_machine.report()
    elif prompt == "off":
        print("The coffee machine is turned off")
        turned_off = True
    else:
        if coffe_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffe_maker.make_coffee(item)

