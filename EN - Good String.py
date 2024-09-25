for fi in range(int(input())):
    n=int(input())
    s=input()
    res=n-1 
    for i in range(n):
        if s[i]=='>' or s[n-1-i]=='<':res=min(i,res)
    print(res)