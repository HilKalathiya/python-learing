# def swap_case(s):
#     string = ""
#     for i in s:
#         if i.isupper()==True:
#             string += i.lower()
#         else:
#             string += i.upper()
#     return string
# s = input("Please:")
# swap = swap_case(s)
# print(swap)
# def count_substring(string, sub_string):
#     count1 = 0
#     for i in range(len(string)-len(sub_string)+1):
#         print(string[i : len(sub_string) + i])
#         if string[i:len(sub_string)+i] in sub_string:
#             count1 += 1
#     return count1

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()

#     count = count_substring(string, sub_string)
#     print(count)
# s="hil kalthiya"
# print(s.split(' '))
s = input()
print("isalnum:", [i.isalnum() for i in s])
print("isalpha:", [i.isalpha() for i in s])
print("isdigit:", [i.isdigit() for i in s])
print("islower:", [i.islower() for i in s])
print("isupper:", [i.isupper() for i in s])
numbers = [0, 1, 2, 3, 4]
result = any(num > 2 for num in numbers)
print(result)
