t=int(input())
arr = list(map(int,input().split()))
for i in arr:
    if i/14>=1 and 1<=i%14<=6:
        print("YES")
    else:
        print("NO")