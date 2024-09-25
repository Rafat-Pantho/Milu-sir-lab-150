s=input()
n=[]
for i in s:
    if i !="+":
        n.append(int(i))
n.sort()
a=""
for i in range(len(n)):
    a=a+str(n[i])
    if i+1<len(n):
        a=a+"+"
print(a)