name = "Hil Kalathiya"
friend = "Chetan Gadhiya"
otherFriend = "Sahaj"
print("hello," + name + friend + otherFriend)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])
print(name[9])
print(name[10])
print(name[11])
print(name[12])
# print(name[13])  # this will through error
for hil in name:
    print(hil)


# to  convert string into list use "split()"or s=list(string) and to convert list into string use "join()"


# lecture = 12

hil = "Hilkalthiya"
if "Hi" in hil:  # for checking something that is in string or not
    print("Yes")

fruits = "mango,apple,pineapple,banana"
print(len(fruits))
m = len(fruits)  # also
print(m)
print(
    fruits[0:6]
)  # this includes 0 but not include 6th character and counting is start from 0
print(fruits[:6])  # same
print()
print(fruits[-10:20])  # ahi -10 atle string ni length mathi 10 bad kari
# je number ave tya thi 20 sudhi
print((fruits[-26 : len(fruits) - 20]))


# lecture = 13

# STRINGS ARE IMMUTABLE they can not be changed
# pan kai change karvi to teni copy bane che
a = "hil bharatbhai kalathiya"
print(
    a.upper()
)  # have ane kai fruits string ma change nathi kariyo pan fruits.upper() name ni copy bani che
print(a)  # you see na

b = "HIL CHETAN SAHAJ"
print(b.lower())
print(b)

c = "/////ghanshyam//////"
print(
    c.strip("/")
)  # aa "strip" name nu fuction teni anndar je kai nakhavi to te String mathi te vastu agal ane pachal thi kadhi nakhe che

print(c.rstrip("/"))  # aa "rstrip" name nu fuction khali pachal nu kadhe

print(
    a.replace("hil", "jagrut")
)  # "replace" fuction ma pahela je lakhavi tene pachi je lakhavi tena thi replace kari de ane jetli var karvu hoy tetli var kari de che
# pan je case ma tame name lakhiyu hoy tene j replace kare tenathi alag case na ne no kare

print(
    a.split(" ")
)  # "split" name nu function te teni ander je lakvi te jo string ma dekhay to syathi split kari teni list banavi de che
d = "hil~good~boy"
d = d.split("~")
print(d)  # you see

d = "-".join(d)  # to joint a list to a string


e = "information about python"
print(
    e.capitalize()
)  # "capitalize" function te string na khali pahela shabd ne capital kare ane baki na badha ne small kari de che
f = "iFORMATION ABOUT PYTHON"
print(f.capitalize())  # you see

g = "Jay Swaminarayan!!"
print(g.center(50))
print(len(g))
print(
    len(g.center(50))
)  # samjiyu kai ahi "center" function a teni andar jetlu nalkhvi tetla length ni string ne banve
# che ane banavva mate spACE add kare che pan te tene center ma rekhe che
print(g.center(50, "."))  # you see kem center ma rekhe che
print(g.center(50, "~"))
print(g.count("Jay"))  # out put lo samji jaso


h = "Hi I am Hil Kalathiya an I am learning python."
print(
    h.endswith(".")
)  # aa ek boolean type nu fuction che jema andr nakhelu end ma che ke nahi te kahrshe
print(
    h.endswith("Hil", 0, 11)
)  # ama apde 0 to 11 ma check kariyu ke Hil chhelle che ke nahi am pan thay
print(
    h.find("I")
)  # aa pahili var je vastu laki che te kya che find kari tenu index appe che
#  jo andar mukeli vastu String ma na hoy to -1 ape che
print(h.find("hile"))
# print(h.index("Hile")) # aa exact find jevu che khali jo andr no sabd na male to error ape che

i = "HiHilKalathiya09"
print(
    i.isalnum()
)  # ahi "isalnum" te A-Z,a-z and 0-9 no j upyog thayo che ke nahi te janva boolean function che space pan na chale
print(i.isalpha())  # aa khali A-Z and a-z nu jove
i = "hil kalathiya"
print(i.islower())  # checke kare ke tena badha lower che ke nahi

i = "hil \n"
print(
    i.isprintable()
)  # aa kahe ke tena badha character printable che ke nahi \n \t jeva pritable nathi atle false ave

i = "           "
print(i.isspace())  # a khali space hoy to true nahi tar false


i = "Hi I Am Hil Kalathiya"
print(
    i.istitle()
)  # a check kare ke string na badha word no first character capital che ke nahi hoy to true nahitar false
i = "Hi I Am Hil kalathiya"
print(i.istitle())

str1 = "WORLD HEALTH ORGANIZATION"
print(str1.isupper())  # check kare ke upper ma che ke nahi

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))  # jota khabar pade

str1 = "Python is a Interpreted Language"
print(str1.swapcase())  # jota khabar pade

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())  # aa baddha word na pahela akhar ne capitakari de che
