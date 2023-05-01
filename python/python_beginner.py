# Variables
a = 1
b = 5
name = "Alex"

# Conditionals
if (a < b):
    print("a is indeed less than b")
elif (b < a):
    print("b is less than a")
else:
    print("a and b are probably equal")

# Chained conditionals
if (a < b):
    if (name == "Alex"):
        print("Hi Alex")
    else:
        print("Oh, you're not alex")

# Operators
x = ((10 + 2) - 3)
y = ((x * 2) / 6)
z = (y ** 3)
a = 10 % 3
b = 1
b += 2

print(x, y, z, a, b)

# Lists
students = ["Alex", "Maddie", "Jeff", "Bezos", "John"]
students.remove("Bezos")
students.append("Bill")
students.sort()
print(students, students[0])

# Dictionaries
my_car = {
    "year": "2010",
    "brand": "Mazda",
    "Coolness level": 10
}
my_car["year"] = "2005"
my_car["color"] = "Red"
print(my_car)

# Loops
for x in students:
    print(x)
    if x == "Jeff":
        break

iterator = 0
while iterator <= 4:
    print(students[iterator])
    iterator +=1

# Functions
def change_car_color(my_car, color):
    my_car["color"] = color
    return True

print(change_car_color(my_car, "Yellow"))
print(my_car)


