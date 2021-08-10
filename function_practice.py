def percentage(marks):
    return ((marks[0] + marks[1] + marks[2] + marks[3]) / 400) * 100


mark1 = [66, 77, 80, 90]
mark2 = [55, 44, 77, 66]
student1 = percentage(mark1)
print("Percentage of student1: ", student1)
student2 = percentage(mark2)
print("Percentage of student2: ", student2)


def greeting(name):
    print("Good day " + name)


def addition(number1, number2):
    return number1 + number2


greeting("Dilip")
add = addition(4, 6)
print("Addition of two number by calling the addition function", add)
