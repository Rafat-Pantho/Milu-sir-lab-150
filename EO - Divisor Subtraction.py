def gen(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return i
    return n

n=int(input())
d=0 
if n%2!=0:
    n-=gen(n)
    d+=1
print(d+n//2)