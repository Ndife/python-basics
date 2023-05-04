# import sys
import argparse

# name =  sys.argv[1]
# print('hello', name)


parser = argparse.ArgumentParser(
    description='This program prints the name of my dogs'
    )

parser.add_argument('-c', '--color', metavar='color', required=True, choices={ 'yellow', 'orage', 'black'},
help='the color to searh for')

parser.add_argument('-a', '--age', metavar='age', required=True, choices={ '20', '40'},
help='shows your age')


args = parser.parse_args()

print(args.color)
print(args.age)
