a = input("enter first number:")
b = input("enter second number:")

# conversion of input value into int
a = int(a)
b = int(b)

a = a * a
b = b * b
# Use the new f-string formatting in Python
print(f'square of a: {a} and b: {b}')
avg = (a + b) / 2
print("The average of a and b is:", avg)
