""" Dog module

this module odes .........
following classes: 

- Dog

...

"""

def increment(n):
    """Increment a number"""
    return n + 1


class Dog: 
    """A class representing a Dog"""
    def __init__(self, name, age):
        """initialize a new dog"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print("Wof!")

print(help(Dog))