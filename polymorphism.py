# two classes having the same child method 

class Dog: 
    def eat(self):
        print('dog eating...')

class Goat: 
    def eat(self):
        print('goat eating...')

animal1 = Dog()
animal2 = Goat()

animal1.eat()
animal2.eat()