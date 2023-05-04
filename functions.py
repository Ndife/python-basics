def hello(name="my friend"):
    print('Hello!', name)

def hey(name, age):
    print(f"hey {name} you are {str(age)} old")

# hey('son', 49)

def change(value): 
    value['name'] = 'syd'

val = {'name': 'ben'}
change(val)

# print(val)

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

# talk('I am going to buy the milk')

def counter():
    count = 1

    def increment():
        nonlocal count
        count += 1
        print(count)

    increment()

counter()