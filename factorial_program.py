# The factorial of a number is the function that multiplies the number by every natural number below it.
# 4!=4*3*2*1
# recursive factorial:  recursive is a function which calls itself
# n!=n*(n-1)
def factorial_iterative(num):
    product = 1
    for i in range(num):
        product = product * (i + 1)
    return product


def factorial_recursive(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial_recursive(num - 1)


number = int(input("Enter number for factorial without recursive: "))
factorialNumber = factorial_iterative(number)
print(f" factorial of given number {number} without recursive is:", factorialNumber)

number = int(input("Enter number for factorial with recursive: "))
factorialNumber = factorial_recursive(number)
print(f" factorial of given number {number} with recursive is:", factorialNumber)
