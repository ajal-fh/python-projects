class CoffeeMachine:
    def __init__(self):
        self.money_collected = 0  # money in dollars
        self.display()
    __MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
                "milk": 0,
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

    __resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    def printStatus(self):
        print("Water: {}ml:".format(self.__resources["water"]))
        print("Milk: {}ml".format(self.__resources["milk"]))
        print("Coffee: {}g".format(self.__resources["coffee"]))
        print("Money: $", self.money_collected)

    def makeCoffee(self):
        if (self.checkResources() and self.CheckTransactions()):
            self.__resources["water"] -= self.__MENU[self.user_input]["ingredients"]["water"]
            self.__resources["milk"] -= self.__MENU[self.user_input]["ingredients"]["milk"]
            self.__resources["coffee"] -= self.__MENU[self.user_input]["ingredients"]["coffee"]
            print("Here is your "+ self.user_input +" ☕ Enjoy!")
        else:
            pass



    def checkResources(self):
        if (self.__resources["water"] >= self.__MENU[self.user_input]["ingredients"]["water"]):
            pass
        else:
            print("Sorry there is not enough water")
            return False
        if (self.__resources["coffee"] >= self.__MENU[self.user_input]["ingredients"]["coffee"]):
            pass
        else:
            print("Sorry there is not enough coffee")
            return False
        if (self.__resources["milk"] >= self.__MENU[self.user_input]["ingredients"]["milk"]):
            pass
        else:
            print("Sorry there is not enough milk")
            return False
        return True

    def ProcessCoins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        input_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
        return input_money

    def CheckTransactions(self):
        input_money = self.ProcessCoins()
        if(input_money < self.__MENU[self.user_input]["cost"]):
            print("​Sorry that's not enough money. Money refunded")
            return False
        if(input_money > self.__MENU[self.user_input]["cost"]):
            print("Here is your change : $", str(
                input_money - self.__MENU[self.user_input]["cost"]))
            self.money_collected += self.__MENU[self.user_input]["cost"]
            return True
        else:
            self.money_collected += input_money  # add the money to the machine
            return True

    def display(self):
        while True:
            self.user_input = input(
                "What would you like? (espresso/latte/cappuccino)? ")
            if (self.user_input == 'espresso' or self.user_input == 'latte' or self.user_input == 'cappuccino'):

                self.makeCoffee()
            elif self.user_input == 'off':
                quit()
            elif self.user_input == 'report':
                self.printStatus()
