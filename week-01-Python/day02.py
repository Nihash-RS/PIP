#input in the python
x=input("Enter your name:")
print (x)

#Typecasting in python -Convert datatypes using int(), float(), str()
x=10
print (type(x))

y="Nihash"
print(type(y))

#to CHeck type of z boolean
z=True
print(type(z))

#here can change integer to flaot
x=10
x=float(x)
print(type(x))


#different types so we get false 
a=10
print (a)
z=str(a)
print(a==z)


# String
name = "Nihash"

# Integer
age = 20

# Float
height = 5.8

# Boolean
is_student = True

# List
fruits = ["Apple", "Mango", "Banana"]

# Tuple
colors = ("Red", "Green", "Blue")

# Set
numbers = {10, 20, 30}

# Dictionary
student = {
    "name": "Nihash",
    "age": 20
}

# Checking data types
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(fruits))
print(type(colors))
print(type(numbers))
print(type(student))

#List in python - Ordered Chanagable collection using[]
#List Operations - Chnage ,append, remove, pop, insert, sort, reverse, clear

numbers = [10, 20, 30, 40, 50]
#          0   1   2   3   4
numbers[0] = 200   #by index number 
numbers.append(60) #to add elements
numbers.remove(30) #to remove elements
numbers[2] = 300
print (numbers[0])

