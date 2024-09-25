x,y,z=map(int,input().split())
a,b,c=map(int,input().split())

if x<=a and (x+y)<=(a+b) and (x+y+z)<=(a+b+c):
    print("YES")
else:
    print("NO")