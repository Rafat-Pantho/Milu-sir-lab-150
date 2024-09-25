for fi in range (int(input())):
    a,b,c,r= map(int,input().split())
    L = max(min(a, b), c - r)
    R = min(max(a, b), c + r)
    print( max(a, b) - min(a, b) - max(0, R - L))