n,k=map(int,input().split())
h=sorted(list(map(int,input().split())))
if k>=n:print(0) 
else:
    sum1=0
    for i in range(n-k):
        sum1+=h[i]
    print(sum1)