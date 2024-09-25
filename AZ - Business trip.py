n=int(input())
arr1 =sorted(list(map(int,input().split())))
if n==0: print(0)
else:
    sum1=0
    for i in range(len(arr1)):
        sum1+=arr1[len(arr1)-1-i]
        if sum1>=n:
            print(i+1)
            break
    if(sum1<n):print(-1)