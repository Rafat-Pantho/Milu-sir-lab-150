for fi in range(int(input())):
    n,m=map(int,input().split())
    if n==1 or m==1:print(f"Case {fi+1}:",max(m,n))
    elif n==2 or m==2:print(f"Case {fi+1}:",(m*n)//8*4 + min((m*n)%8,4))
    else: print(f"Case {fi+1}:",(m*n+1)//2)