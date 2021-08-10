number = int(input("Enter number"))

prime = True
for i in range(2, number):
    if number % i == 0:
        prime = False
        break
if prime:
    print(f"{number} number is prime")
else:
    print(f"{number} number is not prime")
