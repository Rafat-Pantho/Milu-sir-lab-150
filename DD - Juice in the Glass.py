from math import acos
pi = 2.0*acos(0.0)
for fi in range(1,int(input())+1):
    r1,r2,h,p=map(int,input().split())
    r3= p/(h*1.0) * (r1-r2) + r2
    volume1= p*pi/3.0 *(r3*r3+r2*r2+r3*r2)
    print(f"Case {fi}: {volume1:.10f}")