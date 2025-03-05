python_dictonary = { 
    "name": "Python",
    "type": "Programming Language",
    "version": "3.8.5",
    "year": "1991",
    "framework": "Django",
    "creator": "Guido van Rossum"
}

# Accessing the values of the dictonary
print(python_dictonary["name"])

python_dictonary["loop"] = "for loop"

empty_dictonary = {}

#wiping out the dictonary
# python_dictonary = {}

# print(python_dictonary)

# editing the dictonary

python_dictonary["version"] = "3.9.0"
# print(python_dictonary['version'])
# print(python_dictonary) 

# for thing in python_dictonary:
#     print(thing) 

for key in python_dictonary:
    print(key,  ":",  python_dictonary[key])