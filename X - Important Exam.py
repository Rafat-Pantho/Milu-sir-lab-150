n,m = map(int,input().split())
s=[input() for i in range (n)]
d= list(map(int,input().split()))
b=[[0]*5 for i in range(m)]
ans=0 
for i in range(m):
    for j in range(n):
        b[i][ord(s[j][i])-ord('A')]+=1
    ans+=max(b[i])*d[i]
print(ans)