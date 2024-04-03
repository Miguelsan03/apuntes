from abc import ABC, abstractmethod

class IPizza(ABC):

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass

class PizzaNapolitana(IPizza):

    def prepare(self):
       print("Se esta preparando la pizza napolitana") 

    def bake(self):
       print("Se esta horneando la pizza napolitana")

    def cut(self):
       print("Se esta cortando la pizza napolitana")
    
    def box(self):
       print("Se esta empacando la pizza napolitana")

class PizzaHawaiana(IPizza):

    def prepare(self):
       print("Se esta preparando la pizza hawaiana") 

    def bake(self):
       print("Se esta horneando la pizza hawaiana")

    def cut(self):
       print("Se esta cortando la pizza hawaiana")
    
    def box(self):
       print("Se esta empacando la pizza hawaiana")

## esta clase es la encargada de seleccionar la pizza, quedando la clase principal libre - abierto/cerrado
class SimplePizzaFactory():
    def selectPizza(self, type):
        if type == 'napolitana':
            pizza=PizzaNapolitana()
        elif type == 'hawaiana':
            pizza=PizzaHawaiana()
        return pizza

class PizzaStore():

    def orderPizza():
        factory = SimplePizzaFactory()
        pizza = factory.selectPizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

if __name__ == '__main__'