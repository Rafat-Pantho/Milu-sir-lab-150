n= int(input())
a=[int(i) for i in input().split()]
a.sort()
sum1 = sum(a[0:(n//2)])
sum2 = sum(a[(n//2)::])
print(sum1*sum1 + sum2*sum2)