for fi in range(int(input())):
    n,s,k=map(int,input().split())
    a=list(map(int,input().split()))
    if s not in a: print(0)
    else:
        for i in range(k+1):
            if s-i>=1 and s-i not in a:
                print(i)
                break
            if s+i<=n and s+i not in a:
                print(i)
                break