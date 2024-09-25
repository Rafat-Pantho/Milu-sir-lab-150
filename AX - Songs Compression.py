n,m=map(int,input().split())
sum1=0 
sum2 =0
count=0
arr_of_y=[]
for i in range(n):
    x,y=map(int,input().split())
    sum1+=x
    arr_of_y.append(x-y)
arr_of_y.sort()
if sum1<=m:
    print(0)
else:
    while n>0:
        sum2+=arr_of_y[n-1]
        count+=1
        n-=1
        if sum1-sum2<=m:
            print(count)
            break
    if sum1-sum2>m:
        print(-1)
