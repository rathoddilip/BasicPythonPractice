# difference between tuples and list is that we cannot change the value of tuples
tup = (1, 2, 5, 6, 1)
print(tup)

# wrong way of single tuple declaration
# t = (1)
# right way of single element tuple declaration
t1 = (1,)
print(t1)

# methods
print(tup.count(1))  # this will print number of time 1 is occurrences
print(tup.index(5))  # this will return index no of 5
