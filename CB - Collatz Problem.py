s=int(input())
m=[s]
if s<3:print(4)
else:
    while s>1:
        s= 3*s+1 if (s%2) else s//2
        if m.count(s)>1:
            break
        else:m.append(s)
    print(len(m)+1)