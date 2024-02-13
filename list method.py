l = [3, 4, 2, 1, 34, 5, 6, 7, 8, 4, 43, 4, 45,1,3,2]
l.append(23)
print(l)
l.pop(4) # remove item at that index if we can not input anything then it defult remove last element
print(l)
l.remove(3) # in remove we have to give input in the remove by that it is different from pop
print(l)
# l.append("Hil")
l.sort()
print(l)
l.sort(reverse = True)
print(l)
l.reverse()
print(l)
print(l.index(3)) # aa 3 number kya che teni index batave che and gives first occurrence
print(l.count(3)) # aa 3 ketli var ave che te print kare che

m = l 
m[12] = 0
print(l)  # you see that by this if you change m then l is also changed

m = l.copy()  # now m is become copy of l so we can change m with out changing l
m[12] = 0
print(l) 
print(m)
l.insert(2,293)  # aa 2 index par 293 insert kari dese
print(l)

n = [32,12,32,4,33]
l.extend(n)  # aa l na end ma n ne add kari dese
print(l)
b = l + n # this is for when you don't want to change your i so it work like make new list
print(b)