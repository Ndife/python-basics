

dog = { "name": 'ruby', "city": "lagos", "age": 8, "color": "black" }

dog["name"] = "kep"

dogCopy = dog.copy()

print(dog['name'])
print(dog.get('color', 'brown'))

print(dog.popitem())  #pop and show the removed item
dog.pop('name')
print(dog)
print('age' in dog)
print(dog.keys())
print(list(dog.keys()))
print(dog.values())
print(list(dog.values()))
print(list(dog.items()))

dog["man's favourite food"] = 'Egusi'
del dog['age']
print(dog)

print(dogCopy)