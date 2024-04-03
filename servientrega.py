from abc import ABC, abstractmethod

class ITransport(ABC):

    @abstractmethod
    def deliver(self):
        pass

class Truck(ITransport):

    def deliver(self):
        print('Se esta entregando por camion')

class Ship(ITransport):

    def deliver(self):
        print('Se esta entregando por barco')

class Train(ITransport):

    def deliver(self):
        print('Se esta entregando por tren')

class Logistic(ABC):

    def plan_delivery(self):
        transport = self.createTransport()
        transport.deliver

    @abstractmethod
    def createTransport(self) -> ITransport:
        pass

class RoadLogistic(ABC):
    def createTransport(self) -> ITransport:
        return Truck()
    
class SeaLogistic(ABC):
    def createTransport(self) -> ITransport:
        return Truck()