
# example 1:

try:
    result = 2 / 0
except ZeroDivisionError:
    print('number can not be divided by 0')
else: 
     print(result)

# example 2:

try:
    result = 2 / 0
except ZeroDivisionError:
    print('number can not be divided by 0')
finally:
    result = 1

print(result)

# example 3:

try: 
    raise Exception('An error!')
except Exception as error:
    print(error)


# example 4:

class DogNotFoundException(Exception):
    print("inside")
    pass        #must be used when defined a class without methods or functions without body/code

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found')


# example 5: using with
# with automatically closses the file after reading it

filename = '/Users/ndifeuchenna/documents/newfile.rtf'

with open(filename, 'r') as file:
    content = file.read()
    print(content)


# the traditional way of reading a file 

# try:
#     file = open(filename, r)
#     content = file.read()
#     print(content)
# finally: 
#     file.close()