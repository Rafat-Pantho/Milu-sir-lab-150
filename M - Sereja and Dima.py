n= int(input())
a=list(map(int,input().split()))

count_1=0
count_2=0
for i in range(n):
    if i%2==0:
        count_1+=max(a[0],a[len(a)-1])
        a.pop(0 if a[0]>=a[len(a)-1] else (len(a)-1))
    else:
        count_2+=max(a[0],a[len(a)-1])
        a.pop(0 if a[0]>=a[len(a)-1] else (len(a)-1))
print(count_1,count_2)    