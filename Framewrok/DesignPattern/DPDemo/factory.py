from abc import abstractmethod, ABC


###################### [1] ######################
class Pizza(ABC):

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("baking pizza for 12min in 400 degrees..")

    def cut(self):
        print("cutting pizza in pieces")

    def box(self):
        print("putting pizza in box")


class CheesePizza(Pizza):
    def prepare(self):
        print("preparing a cheese pizza..")


class GreekPizza(Pizza):
    def prepare(self):
        print("preparing a greek pizza..")


def orderPizza(pizzaType: str):
    # orderPizza needs to be aware of the pizza creation task.
    # this is violating the single responsibility principle
    # since our code is open for modification
    if pizzaType == 'Greek':
        pizza = GreekPizza()
    elif pizzaType == 'Cheese':
        pizza = CheesePizza()
    else:
        print("No matching pizza found...")

    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()


print("##### [1] ########")
orderPizza('Greek')
print("##################\n")


#################################################
###################### [2] ######################

# We can instead create a Simple Factory that will
# exclusively deal with the pizza creation process.
class SimplePizzaFactory:

    def createPizza(self, pizzaType: str) -> Pizza:
        pizza: Pizza = None

        if pizzaType == 'Greek':
            pizza = GreekPizza()
        elif pizzaType == 'Cheese':
            pizza = CheesePizza()
        else:
            print("No matching pizza found...")

        return pizza


class PizzaStore:
    factory: SimplePizzaFactory

    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    def orderPizza(self, pizzaType: str):
        # orderPizza only needs to be aware of preparing the pizza.
        # we have encompassed everything
        pizza: Pizza
        pizza = self.factory.createPizza(pizzaType)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()


#################################################
store = PizzaStore(SimplePizzaFactory())

print("##### [2] ########")
store.orderPizza('Greek')
print("##################\n")