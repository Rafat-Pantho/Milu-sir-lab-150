def is_ramaji(s):
    if s[-1] not in "aeioun":
        return False
    for i in range(len(s)-1):
        if s[i] not in "aeiou" and s[i+1] not in "aeiou":
            if s[i]!="n":
                return False
    return True
        
s= input()
print("YES" if is_ramaji(s) else "NO")