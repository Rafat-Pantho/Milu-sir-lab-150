n= int(input())
a=[int(i) for i in input().split()]
a.sort()
count=0
for i in range(n-1):
    count += ((a[i+1]-a[i])-1)
print(count)