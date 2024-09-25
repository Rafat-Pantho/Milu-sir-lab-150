n=int(input())
s=input()
for i in s:
    x= (ord(i)-ord('A')+n)%26
    print(chr(x+ord('A')),end='')
print()