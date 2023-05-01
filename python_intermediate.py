# List comprehension
students = ["Alex", "Maddie", "Jeff", "Bezos", "John"]
selected_students = [x for x in students if "a" in x.lower()]
print("List Comprehension: ", selected_students)

# Dictionary comprehension
students_and_gpa = {x: len(x) for x in students if "j" in x.lower()}
print("Dictionary comprehension: ", students_and_gpa)

# Lambda Functions
func1 = lambda x: "Dr. " + x
print("Lambda: ", func1(students[0]))

# Map function
new_list = list(map(func1, students))
print("Map: ", new_list)

# Filter function
newer_list = list(filter(lambda  x: "a" in x.lower(), students))
print("Filter: ", newer_list)

# Args (*args not mutable)
def sum(*args):
    total = 0
    for x in args:
        total += x
    return total

total = sum(1, 3, 4)
print("*args: ", total)

# Kwargs
def sentence_maker(**kwargs):
    full_sentence = ""
    for x in kwargs.values():
        full_sentence += x
        full_sentence += " "
    return full_sentence

sentence = sentence_maker(a = "Hello", b = "my", c = "friend.")
print("**kwargs: ", sentence)