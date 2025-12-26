import copy
s=[1,2,[300,300]]
s2=copy.deepcopy(s)
s[2][0]=500
print(s)
print(s2)
