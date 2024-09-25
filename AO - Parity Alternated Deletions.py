t=int(input())
s=sorted(list(map(int,input().split())))
a=[x%2 for x in s]
if a.count(1)==a.count(0) or abs(a.count(1)-a.count(0))==1:
    print(0)
elif a.count(1)>a.count(0):
    summing =0
    n=0
    i=0
    while n< a.count(1)-a.count(0)-1:
        if s[i]%2==1:
            summing+=s[i]
            n+=1
        i+=1
    print(summing)
elif a.count(1)<a.count(0):
    summing =0
    n=0
    i=0
    while n< a.count(0)-a.count(1)-1:
        if s[i]%2==0:
            summing+=s[i]
            n+=1
        i+=1
    print(summing)