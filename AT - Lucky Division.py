def is_lucky(n):
    if n%4==0 or n%7==0:
        return True
    
    i=47 
    while i<=n:
        if i%7==0:i+=2
        if all(a in "47" for a in str(i)) and n%i==0: return True
        i+=2
    
    return False

n=int(input())
print("YES" if is_lucky(n) else "NO")