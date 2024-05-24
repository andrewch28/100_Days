from Menu import MENU, resources

def main():
    money = 0
    drinks = ['espresso', 'latte', 'cappuccino']
    while True:
        order = input(" What would you like? (espresso/latte/cappuccino): ")

        if order == 'report':
            report(money)

        elif order == 'off':
            break

        elif order in drinks:

            for item in resources:
                if resources[item] - MENU[order]["ingredients"][item] < 0:
                    print(f'Sorry, there is not enough {item}')
                    break
            else:
                change = check(order)
                if change != False:
                    money += MENU[order]["cost"]
                    print(f'Here is ${round(change, 2)} in change')
                    print(f'Here is your drink☕ !')
                    for item in resources:
                        resources[item] -= MENU[order]["ingredients"][item]


def report(money):
    print(f'Water: {resources['water']}ml')
    print(f'Milk: {resources['milk']}ml')
    print(f'Coffee: {resources['coffee']}g')
    print(f'Money: ${money}')


def check(drink):
    """Checks whether there are enough coins inserted"""
    print('Please insert coins.')
    coins = {'quarters' : 0, 'dimes' : 0, 'nickles' : 0, 'pennies' : 0}
    for i in coins:
        coins[i] = int(input(f'How many {i}? '))
    sum = 0.25 * coins['quarters'] + 0.1 * coins['dimes'] + 0.05 * coins['nickles'] + 0.01 * coins['pennies']
    if MENU[drink]['cost'] <= sum:
        change = sum - MENU[drink]['cost']
        return change

    else:
        print("Sorry that's not enough. Money refunded")
        return False

main()