for fi in range (int(input())):
    n,k=map(int,input().split())
    x=n-n%k
    x+=min(n%k,k//2)
    print(x)