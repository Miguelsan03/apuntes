from abc import ABC, abstractmethod

class ICharacter(ABC):
    @abstractmethod
    def render(self):
        pass

class IEnemy(ABC):
    @abstractmethod
    def attack(self):
        pass

class IObstacle(ABC):
    @abstractmethod
    def block(self):
        pass

class EasyCharacter(ICharacter):
    def render(self):
        print("Renderizando personaje facil")

class HardCharacter(ICharacter):
    def render(self):
        print("Renderizando personaje dificil")

class EasyEnemy(IEnemy):
    def attack(self):
        print("Enemigo facil atacando")

class HardEnemy(IEnemy):
    def attack(self):
        print("Enemigo dificil atacando")
        
class EasyObstacle(IObstacle):
    def render(self):
        print("Renderizando obstaculo facil")

class HardObstacle(IObstacle):
    def render(self):
        print("Renderizando obstaculo dificil")

class IlevelFactory(ABC):
    @abstractmethod
    def create_character(self):
        pass
    
    @abstractmethod
    def create_enemy(self):
        pass
    
    @abstractmethod
    def create_obstacle(self):
        pass

class EasyLevelFactory():
    def create_character(self):
        return EasyCharacter()
    def create_enemy(self):
        return EasyEnemy()
    def create_obstacle(self):
        return EasyObstacle()
    
class HardLevelFactory():
    def create_character(self):
        return HardCharacter()
    def create_enemy(self):
        return HardEnemy()
    def create_obstacle(self):
        return HardObstacle() 
        
def playLevel(factory:IlevelFactory):
    character = factory.create_character()
    enemy = factory.create_enemy()
    obstacle = factory.create_obstacle()

    character.render()
    enemy.attack()
    obstacle.render()