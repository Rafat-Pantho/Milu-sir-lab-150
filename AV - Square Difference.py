def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
for fi in range(int(input())):
    a,b=map(int,input().split())
    print("YES" if abs(a-b)==1 and is_prime(a+b) else "NO")