from math import ceil
for fi in range(int(input())):
    n=int(input())
    sa=list(map(int,input().split()))
    s=[2]
    s.extend(sa)
    count=0
    for i in range(1,len(s)):
        count+=(s[i]-s[i-1]+4)//5
    print(f"Case {fi+1}:",count)