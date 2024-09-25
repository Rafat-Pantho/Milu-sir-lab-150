for fi in range(int(input())):
    r1 ,c1, r2, c2=map(int,input().split())
    c=abs(c1-c2)
    r=abs(r1-r2)
    if r==c:print(f"Case {fi+1}: 1")
    elif r%2==c%2:print(f"Case {fi+1}: 2")
    else:print(f"Case {fi+1}: impossible")