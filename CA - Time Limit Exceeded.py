import math

N,T=map(int,input().split())
ans=math.inf

for i in range(N):
    c,t=map(int,input().split())
    if t<=T and c<ans:
        ans=c

print("TLE" if ans==math.inf else ans)