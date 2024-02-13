a = int(input("Enter Your Age:"))
b = input("Enter Your Gender:")
def vote_gender():
    if b == "female":
        if a >= 18:
            print("'You are eligible to vote'")
            c = input("Do you want to Marry:")
            if c == "yes":
                print("Then You Can Marry to Good Life Partner For Your Self")
            else:
                print("Ok Your Life Your Rules Very Good! ")
        else:
            print("You are not eligible to vote")
            print("And if you want to marry or not but can't eligible to do")
    elif b == "male":
        if a >= 18:
            print("'You are eligible to vote'")
            print("But sorry you can't eligible to marry wait for some years if you want")
        elif a >= 21:
            print("'You are eligible to vote'")
            c = input("Do you want to Marry:")
            if c == "yes":
                print("Then You Can Marry to Good Life Partner For Your Self")
            else:
                print("Ok Your Life Your Rules Very Good! ")
        else:
            print("You are not eligible to vote and marrage")
  
       
                
                
      