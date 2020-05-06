from abc import ABC, abstractmethod

class Eat(ABC):
    @abstractmethod
    def juice(self):
        pass

class Fruit(Eat):
    def juice(self):
        print('Fruit Juice: So Tasty')

class Vegetable(Eat):
    def juice(self):
        print('Vegetable Juice: Not so tasty')

popo = Fruit()
popo.juice()
jojo = Vegetable()
jojo.juice()
