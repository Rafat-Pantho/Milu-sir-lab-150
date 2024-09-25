n=int(input())
s=[]
for i in range(n):
    s.append(int(input()))
print(sum(s)-max(s)//2)