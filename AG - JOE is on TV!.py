n=int(input())
ans=0
while n>0:
    ans+=1/n
    n-=1
print("{:.12f}".format(ans))