# def nested_list():
#     # l1 = []
#     # l2 = []
#     l1=[[input("n"), float(input("s"))] for i in range(int(input("N")))]
#     print(l1)
#     l1.sort()
#     print(l1)
#     print(l1[1])
# nested_list()
def count_substring(string, sub_string):
    string = list(set(string))
    sub_string = list(set(sub_string))
    count = 0
    for i in range(len(string)):
        for j in range(len(sub_string)):
            if string[i] == sub_string[j]:
                count += 1
    return count


# if __name__ == '__main__':
string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)
