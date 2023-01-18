from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
coffee_maker = CoffeeMaker()
m = Menu()
while True:
    c_name = input(f"Enter coffee name {m.get_items()}: ")
    if c_name == "report":
        coffee_maker.report()
        money.report()
    if c_name == "off":
        coffee_maker.report()
        money.report()
        break
    else:
        drink = m.find_drink(c_name)
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
