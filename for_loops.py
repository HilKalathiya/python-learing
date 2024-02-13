name = "Abhishek"
for i in name:
    print(
        i, end=", "
    )  # a loop ma ek ek character print karshe ane darek character ni end ma comma print karshe

name = "Abhishek"
for i in name:
    print(
        i
    )  # a loop ma ek ek character print karshe bas khali A uppar ni line ma hashe kem ke \n nathi

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color, end="~") # list na ek element print thase
    for i in color:
        print(i)
    
for num in range(10): # ahi num a 0 thi 10 -1 print karshe
    print(num)
for num in range (1,2000,10):  # ahi num 1 to 2000-1 print karshe pan in step of 10
    print(num)