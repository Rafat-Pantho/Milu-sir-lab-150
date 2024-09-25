for fi in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split() if int(i)<=2048]
    a.sort()
    print("YES" if sum(a)>=2048 else "NO")