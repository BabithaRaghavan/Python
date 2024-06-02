
# Displays Icecreanm flavour and toppings
class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        self.vanila = [self.ingredients[0], self.toppings[0]]
        self.chocolate = [self.ingredients[1], self.toppings[0]]
        return (self.vanila, self.chocolate)


if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

