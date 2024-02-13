# # with argument function no return
# def Gmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
# def isGreater(a,b):
#     if a > b:
#         print("first Number is greater than second Number ")
#     elif a < b:
#         print("second Nuber is greater than first Number ")
# def isLess(a,b):
#     pass  # aa etla mate che ke jo mare a fi=unction ni body pachi kyarek lakhvi hoy ne atyare khali rakhva mate thay che
# a = int(input("Number A:"))
# b = int(input("Number B:"))
# c = int(input("Number C:"))
# d = int(input("Number D:"))
# Gmean(a,b)
# isGreater(a,b)
# Gmean(c,d)
# isGreater(c,d)

# def vowel_consonant(a):  # this is function to find the vowel and the consonant
#     i = 10
#     while i <= 13:
#         if 65 <= ord(a) <= 90 or 97 <= ord(a) <= 122:
#             break
#         else:
#             a = input("Enter a character only not number or spacial character:")
#         i -= 1
#     if (65 <= ord(a) <= 90 or 97 <= ord(a) <= 122) and (
#         ord(a) != 65,
#         ord(a) != 69,
#         ord(a) != 73,
#         ord(a) != 79,
#         ord(a) != 85,
#         ord(a) != 97,
#         ord(a) != 101,
#         ord(a) != 105,
#         ord(a) != 111,
#         ord(a) != 117,
#     ):
#         print(" This is Consonant:", a)
#     elif (
#         ord(a) == 65,
#         ord(a) == 69,
#         ord(a) == 73,
#         ord(a) == 79,
#         ord(a) == 85,
#         ord(a) == 97,
#         ord(a) == 101,
#         ord(a) == 105,
#         ord(a) == 111,
#         ord(a) == 117,
#     ):
#         print("This is vowel:", a)
# char = input("Enter a character:")
# vowel_consonant(char)


# print(ord('c'))
# print(chr(44))  # ord() character ne int ma ferve ane chr() int ne chr ma freve


def avg(a=6, b=9):
    print("Average", (a + b) / 2)


avg(b=9)  # joyu to samji gaya
avg(9)  # am kari ne apde khali a ni value fix kari sakvi
avg(b=0, a=10)  # aam kari ne apde order meter na karavi shakvi


def rag(*num):
    sum = 0
    print(type(num))
    for i in num:
        sum += i
    print(sum / len(num))


rag(
    1, 3, 2, 35, 6, 3, 3, 543, 45, 3, 45, 245, 2, 45, 5, 64, 4, 5, 56
)  # ahi *num lakhva thi teni type "tuple" thai gai che ane pachi tenu kam kariyu che


def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="Buchanan", lname="Barnes", fname="James") #a ** te dictionary datatype banave
