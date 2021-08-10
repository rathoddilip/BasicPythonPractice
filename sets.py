# set is collection of non repetitive element
a = {1, 3, 5, 2, 3, 6}
print(a)

# create empty set and add element
set1 = set()
print(type(set1))
# we cannot add dictionary and list in set
# we can add tuples in set
set1.add(4)
set1.add(4)
set1.add(5)
set1.add((4, 6, 3,))
print(set1)
print("length of set", len(set1))
print("remove element from set", set1.remove(4))
print(set1)
