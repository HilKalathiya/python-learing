def match_():
    x = input("Enter your grade like'O,A+,B+,C+,D+' and F:")
    y = int(input("Enter number:")) # so we can give multipale defult and give codition to them 
    match x:
        case "O":
            print("Exilent grade")
        case "A+":
            print("very good grade")
        case "B+":
            print("good grade")
        case "C+":
            print("Avrage grade")
        case "D+":
            print("poor grade")
        case _:
            print("your your disapoiment")
 
    match y:
        # if x is 0
        case 0:
            print("x is zero")
        # case with if-condition
        case 4 if y % 2 == 0:
            print("y % 2 == 0 and case is 4")
        # Empty case with if-condition
        case _ if y < 10:
            print("y is < 10")
        # default case(will only be matched if the above cases were not matched)
        # so it is basically just an else:
        # ane upper nu defult ptint thay to niche nu na thay skip thay
        case _:
            print(y) 
match_()
