from collections import *

n= int(input())
s=[input()[0] for i in range(n)]
countiog_s=Counter(s)
countings = 0
for i in countiog_s.values():
    a=i//2
    b=i-a
    countings += (a*(a-1)+b*(b-1))//2
print(countings)