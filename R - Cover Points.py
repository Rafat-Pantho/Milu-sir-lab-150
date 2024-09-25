ans=0
for i in range(int(input())):
    x, y = map(int, input().split())
    ans=max(ans,x+y)
print(ans)