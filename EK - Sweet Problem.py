for fi in range(int(input())):
    a=sorted(list(map(int,input().split())))
    print(sum(a)//2 if a[2]<=a[0]+a[1] else a[0]+a[1])