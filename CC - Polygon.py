n=int(input())
s=sorted(list(map(int,input().split())))
print("Yes" if s[-1]<sum(s[:-1]) else "No")