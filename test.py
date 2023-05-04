from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

# print (State.ACTIVE.value)

dogs = ['man', 2, 'ad', 4]
dogs.append("object") 
dogs.extend(['iterable', 3])
dogs += ['new', 55]
dogs.remove(55)
dogs.pop()

dogs.insert(1, 'new object')
dogs[1:1] = ['ok', 'not ok']


items = ['bob', 'man', "BAB", "Chain", "Zan"]
# new_item = items[:]
# items.sort(key=str.lower)
print(sorted(items, key=str.lower))
print(items)
