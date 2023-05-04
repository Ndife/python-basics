from functools import reduce

# map function 
numbers = [1,2,3,4,5,6]

def double(a):
    return a * 2

result = map(double, numbers)

# print(list(result))

# map function using lambda function 
result1 = map(lambda a : a * 2, numbers)
# print(list(result1))


# filter function 
def isEven(n):
    return n % 2 == 0

result2 = filter(isEven, numbers)

# using lambda function
result3 = filter(lambda n: n % 2 == 0, numbers)
# print(list(result2))

# reduce function 

# long way 
expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

sum = 0
for expense in expenses:
    sum += expense[1]

# print(sum)

# simpler way using reduce
sum = reduce(lambda a, b : a[1] + b[1], expenses)

print(sum)