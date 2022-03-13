from machine import *


def accept_coins(money, cost):
    print(f"Cost: ${cost:.2f}")
    print("Please insert coins.")
    num_quarters = int(input("How many quarters?\t"))
    num_dimes = int(input("How many dimes?\t"))
    num_nickels = int(input("How many nickels?\t"))
    num_pennies = int(input("How many pennies?\t"))

    amount_added = 0
    amount_added += num_quarters * 0.25
    amount_added += num_dimes * 0.10
    amount_added += num_nickels * 0.05
    amount_added += num_pennies * 0.01

    print(f"${amount_added:.2f} added.")

    if amount_added >= cost:
        refund = amount_added - cost
        money += amount_added - refund
        print(f"Dispensing change: ${refund:.2f}")
        print("Enjoy!")
        return money
    else:
        refund = amount_added
        print(f"Not enough money inserted. ${refund:.2f} refunded.")
        return money


def make_coffee(resources, coffee_type):
    req_resources = MENU[coffee_type]["ingredients"]
    for resource in req_resources:
        resources[resource][0] -= req_resources[resource]
    print(f"Dispensing: {coffee_type}")


money = 0
user_input = ''
while not user_input == "off":
    user_input = input("What would you like? (espresso/latte/cappuccino)?\t")

    if user_input == "report":
        for resource in resources:
            resource_value = str(resources[resource][0])
            resource_unit = resources[resource][1]
            print(resource.capitalize() + ": " + resource_value + resource_unit)
        print(f"Money: ${money:.2f}")
    elif user_input in MENU:
        selection = MENU[user_input]

        sufficient_resources = True
        for resource in selection["ingredients"]:
            if resources[resource][0] < selection["ingredients"][resource]:
                print(f"Sorry, not enough {resource}.")
                sufficient_resources = False

        if sufficient_resources:
            cost = selection["cost"]
            money = accept_coins(money, cost)
            make_coffee(resources, user_input)

    else:
        print("Invalid input.")
