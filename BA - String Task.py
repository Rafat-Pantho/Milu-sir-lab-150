s=input().lower()
a=""
for i in s:
    if i not in "aeiouy":
        a=a+"."+i
print(a)