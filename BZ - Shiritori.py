n=int(input())
s=[input() for i in range(n)]
for i in range(n):
    if s.count(s[i])>1:
        print("No")
        exit()
    if i!=n-1 and s[i][-1]!=s[i+1][0]:
        print("No")
        exit()
print("Yes")