for fi in range(int(input())):
    a,b=input().split()
    b=abs(int(b))
    rem=0 
    j = 1 if a[0]=='-' else 0
    for i in a[j:]:
        rem = rem*10+int(i) 
        rem%=b
    print(f"Case {fi+1}: divisible" if rem==0 else f"Case {fi+1}: not divisible")