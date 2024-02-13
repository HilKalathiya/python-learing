num = int(input("enter the num:"))
for i in range(15):
    if i == 10:
        break
    if i == 3:
        print("skip the itration")
        continue
    print(num, "x", i + 1, "=", (i + 1) * num)
    