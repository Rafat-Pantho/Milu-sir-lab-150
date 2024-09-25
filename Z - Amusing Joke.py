from collections import Counter

def ans(d,c):
    counting_d=Counter(d)

    for i in c:
        if i in counting_d:
            counting_d[i]-=1
            if counting_d[i]==0:
                del counting_d[i]
        else:
            return "NO"
    return "YES" if not counting_d else "NO"

s=input().strip()
a=input().strip()
c=input().strip()
d = s+a

print(ans(d,c))