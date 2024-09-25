for fi in range(int(input())):
    n,d=map(int,input().split())
    max_time = int(d**0.5)+10
    for x in range(max_time+1):
        if x+(x+d)//(x+1)<=n:
            break
    print("YES" if x<max_time else "NO")