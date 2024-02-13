import time
# big hint ke time.strftime a string ma hoy che tene int ma fervvu pade che time name nu variable na banavvu
def good_morning(a):
    t = time.strftime("%I:%M:%S~%p:%A")
    hour = int(time.strftime("%H"))
    print("This is Time and weekday of today-", t)
    if 5 <= hour < 12:
        print("Good Morning:",a)
    elif 12 <= hour < 18:
        print("Good Afternoon:",a)
    else:
        print("Good Evening:",a)

Name = input("Please Enter Your Name:")
good_morning(Name)
