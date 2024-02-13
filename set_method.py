s1={2,4,3,45,5}
s2 ={6,7,8,2,43}

print(s1.union(s2))  # this give you the union of s1 and s2 jema comman element ke var j avshe like ven diagram
print(s1,s2)  # you see that s1 and s2 are the same they not changed
# for that you have to do s1.update(s2)
s1.update(s2) 
print(s1,s2)# union of s1 and s2 jevu j kam kare che khali s1 ne update kari ne ape che
