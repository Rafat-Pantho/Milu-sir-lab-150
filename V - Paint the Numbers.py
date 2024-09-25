n= int(input())
s=[int(i) for i in input().split()]
s.sort()
a=[]
a.append(s[0])
for i in s:
    find1 = True
    for j in range(len(a)):
        if i%a[j]==0:
            find1 = False
            break
    if find1:
        a.append(i)
print(len(a))