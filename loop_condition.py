i = 0
while i < 10:
    print("Yes " + str(i))
    i = i + 1
print("Done")
# ----------------------------------

fruits = ['banana', 'orange', 'angoes']
j = 0
while j < len(fruits):
    print(fruits[j])
    j = j + 1

# --------------------------
for k in range(8):
    print(k)
    if k == 5:
        break
print("-------------------------")
# specify the start,end and step size

for m in range(1, 8, 2):
    print(m)
