n= int(input())
if n>=0:
    print(n)
else:
    n = abs(n)
    p= int(n/10)
    q= (int(n/100))*10 + (n%10)
    print(max(-p,-q))