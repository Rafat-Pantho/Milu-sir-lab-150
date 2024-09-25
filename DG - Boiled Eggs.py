for fi in range(int(input())):
    n,p,q=map(int,input().split())
    arr1=sorted(list(map(int,input().split())))
    mx=0
    for i in range(n):
        number=bowl=0
        for j in range(i,n):
            if number+1<=p and bowl+arr1[j]<=q:
                bowl+=arr1[j]
                number+=1
                mx=max(mx,number)
            else:
                break
    print(f"Case {fi+1}: {mx}")