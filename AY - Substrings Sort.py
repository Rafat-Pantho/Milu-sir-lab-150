n=int(input())
s=[]
for fi in range(n):
    s.append(input())
s.sort(key = lambda x: len(x))
for i in range(n-1):
    if s[i+1].find(s[i])==-1:
        print("NO")
        exit()
print("YES\n" +"\n".join(s))