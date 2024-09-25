def is_composit(a):
    count=0
    for i in range(2,a):
        if a % i == 0:
            count+=1
    return 1 if count>0 else 0


n= int(input())
b= 4
a=0
while True:
    a=n+b
    if is_composit(a)==1 and is_composit(b)==1:
        break
    b += 1
    while is_composit(b)!=1:
        b+=1

print(a,b)