from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}

coins_value = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

def print_resources(remaining_resources):
    """Print the remaining resources"""
    print(f"water: {remaining_resources["water"]}ml")
    print(f"milk: {remaining_resources["milk"]}ml")
    print(f"coffee: {remaining_resources["coffee"]}g")
    print(f"money: ${remaining_resources["money"]}")

def check_resources(user_request, remaining_resources):
    """Check if there are ingredients remaining to make the drink and return True or False"""
    for key in MENU[user_request]["ingredients"]:
        if MENU[user_request]["ingredients"][key] > remaining_resources[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True

def make_drink(user_request, remaining_resources):
    """Update the machine ingredients and money resources and return them"""
    for key in MENU[user_request]["ingredients"]:
        remaining_resources[key] -= MENU[user_request]["ingredients"][key]
    remaining_resources["money"] += MENU[user_request]["cost"]
    print(f"Here is your {user_request} ☕, enjoy💕!")
    return remaining_resources

def process_coins():
    """Prompt the user to insert the coins and return True if they reach the price or False if they don't """
    coins_inserted = 0
    for key in coins_value:
        coins_inserted += int(input(f"How many {key}?")) * coins_value[key]
    if coins_inserted >= MENU[prompt]["cost"]:
        print(f"Here is ${coins_inserted - MENU[prompt]["cost"]} in change.")
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


# TODO 1) print the remaining resources if the user type "report"
turned_off = False
while not turned_off:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == "report":
        print_resources(resources)

    # TODO 2) stop the execution if the user types "off"
    elif prompt == "off":
        print("The coffee machine is turned off")
        turned_off = True

    else:
        # TODO 3) Check the resources to make the drink selected
        if check_resources(prompt,resources):
            # TODO 4) Prompt the user to insert coins
            print(f"The price of {prompt} is ${MENU[prompt]["cost"]}. Please, insert the coins")
            # TODO 5) Make the drink: update the remaining resources
            if process_coins():
                resources = make_drink(prompt,resources)
        else:
            # go on with the while loop
            continue
