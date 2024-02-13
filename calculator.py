def calc():
    a = int(input("Enter First Number for perform +,*,-,/:"))
    # c = input("input operator:")
    b = int(input("Enter Second Number for perform +,*,-,/:"))

    print("Addition of {} + {} is:".format(a, b), a + b)
    print("subtraction of {} - {} is:".format(a, b), a - b)
    print("Multiplication of {} x {} is:".format(a, b), a * b)
    print("Division of {} / {} is:".format(a, b), a/b)
    print("this is floor division of {} // {} is:".format(a, b), int(a // b))
    print("this is modulo division of {} % {} is :".format(a, b), a % b)
    print("this is exponent of {}^{} is :".format(a, b), a ** b)
    # "input" function is always give output in "string" ,so we have to explicit type conversion
calc()

