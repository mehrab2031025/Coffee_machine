MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

Current_water = 300
Current_milk = 200
Current_coffee = 100
Current_money = 0


def Sufficient_resource(order):
    if Current_water >= MENU[order]["ingredients"]["water"] and Current_milk >= MENU[order]["ingredients"]["milk"] and Current_coffee >= MENU[order]["ingredients"]["coffee"]:
        return True
    else:
        return False

def Sufficient_coin(order):
    print("Please insert coins.")
    c1 = float(input("How many quarters: ")) * 0.25
    c2 = float(input("How many dimes: ")) * 0.10
    c3 = float(input("How many nickle: ")) * 0.05
    c4 = float(input("How many pennie: ")) * 0.01

    global total_money
    total_money = c1 + c2 + c3 + c4
    if total_money >= MENU[order]["cost"]:
        return True
    else:
        return False


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        print(f"Water: {Current_water}ml")
        print(f"Milk: {Current_milk}ml")
        print(f"Coffee: {Current_coffee}g")
        print(f"Money: ${Current_money}")

    elif user_choice == "off":
        exit(1)

    else:
        if Sufficient_resource(user_choice):
            if Sufficient_coin(user_choice):
                Current_water -= MENU[user_choice]["ingredients"]["water"]
                Current_milk -= MENU[user_choice]["ingredients"]["milk"]
                Current_coffee -= MENU[user_choice]["ingredients"]["coffee"]
                Current_money += MENU[user_choice]["cost"]
                print(f"Here is ${round(total_money - MENU[user_choice]["cost"], 2)} in change")
                print(f"Here is your {user_choice}. Enjoy")
        elif Current_water < MENU[user_choice]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        elif Current_milk < MENU[user_choice]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
        elif Current_coffee < MENU[user_choice]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")

