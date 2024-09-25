for fi in range(int(input())):
    w= int(input())
    if w%2:print(f"Case {fi+1}: Impossible")
    else:
        n=w//2
        m=2 
        while n%2==0:
            n//=2
            m*=2
        print(f"Case {fi+1}:",n,m)