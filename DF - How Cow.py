for fi in range(int(input())):
    print(f"Case {fi+1}:")
    x1, y1, x2 ,y2= map(int,input().split())
    m=int(input())
    for i in range(m):
        x,y=map(int,input().split())
        print("Yes" if x>x1 and x<x2 and y>y1 and y<y2 else "No")