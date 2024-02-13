list1 = [3,4,2,1,34,"Hil","chetan","sahaj",True]  # we can store different data types in one list
#  negative indexing ma ahi -1 hoy to length of list minus this num ane je ans male te index par je hoy tene print kari de che
print(list1)
print(list1[0],list1[1],list1[2],list1[3],list1[4])
if "Hil" in list1: # for check something in list
    print("Hil is in the list")
else:
    print("Hil is not in the list")


# list = [ start : end : jump index ]
print(list1[0:9])
print(list1[0:9:2])

# list comprahantion manlab list ne on time banavva nu

n = int(input("Enetr Number:"))
lst = [i for i in range(n)]
print(lst)
lst = [(i * i) / (2 + 3) for i in range(n)]
print(lst)
lst = [(i * i) / (2 + 3) for i in range(n) if (i * i) / (2 + 3) % 2 == 0]  # joy ne khabar padi ne shu thay che
print(lst)
