def gfactors(n):
    x=[]
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            x.append(i)
    x.append(n)
    return x

n= int(input())
arr1=[gfactors(int(i)) for i in input().split()]
print(arr1)
