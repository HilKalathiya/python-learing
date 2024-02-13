tup = (4, 2, 3, 3, 4, 1, 2, 3, 3, 4, 1, 34, 4, 3, 31, "hil", "kalathiya", "sahaj")
# print(tup)
# print(tup[1])
# # tuple = (start:end:jumpindex)
# # tuple ma striping krvi to te tuple ma change nathi thata but new tuple bane che
# print(tup[:11:2])
# print(tup)  # you see
# if "hil" in tup:
#     print("hil is in the tuple")
# else:
#     print("no")


# Tuples are immutable, hence if you want to add, remove or
# change tuple items, then first you must convert the tuple to a list.
# Then perform operation on that list and convert it back to tuple.


countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)  # to change tuple to list
temp.append("Russia")  # add item
temp.pop(3)  # remove item
temp[2] = "Finland"  # change item
countries = tuple(temp)  # to change list to tuple
print(countries)

# However, we can directly concatenate two tuples without converting them to list.

countries1 = ("Spain", "Italy", "India", "England", "Germany")
countries2 = ("pakistan", "afghanistan", "chine")
countries = countries1 + countries2
print(countries)

print(tup.count(3))  # to count that how manytimes 3 is came


# The Index() method returns the first occurrence of the given element from the tuple.
# tuple.index(element, start, end)

print(tup.index(3,1,5))
print(len(tup))
