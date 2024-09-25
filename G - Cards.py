n=int(input())
a= [int(i) for i in input().split()]
a_position =[(a[i],i+1) for i in range(n)]
a_position.sort()

left=0
right=n-1
for i in range(n//2):
    print(a_position[left][1],a_position[right][1])
    left+=1
    right-=1