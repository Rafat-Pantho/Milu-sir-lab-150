for fi in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a.reverse()
    print(min(a[1]-1,n-2))