# The any() function in Python is a built-in function that returns True if at least one element in an iterable
# is True, and False otherwise. It takes an iterable as its argument and evaluates the truthiness of each element in the iterable.


# and ve can put loop into any() in print function like below

s = input()
print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))

# we can also list comprahantion in print function
