import math
for fi in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    result=math.inf
    for i in range(n):
        if a[n-1-i]>result:ans+=1
        result=min(a[n-1-i],result)
    print(ans)