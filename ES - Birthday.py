n=int(input())
s=sorted(list(map(int,input().split())))
arr1=[0]*n
left=0
right=n-1 
for i in range(n):
    if i%2==0:
        arr1[left]=s[i]
        left+=1
    else:
        arr1[right]=s[i]
        right-=1
print(*arr1)