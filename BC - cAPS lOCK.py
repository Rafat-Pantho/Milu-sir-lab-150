a=input()
if(a[0]==a[0].lower() and a[1:]==a[1:].upper()):
    print(a.lower().capitalize())
elif a==a.upper():
    print(a.lower())
else:
    print(a)