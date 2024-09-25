s=input()
t=input()
ans = False
for i in range(len(s)):
    if s==t:
        ans = True
        break
    s=s[-1]+s[:-1]
print("Yes" if ans else "No")