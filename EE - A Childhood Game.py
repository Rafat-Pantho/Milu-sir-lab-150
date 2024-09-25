for fi in range(int(input())):
    n,name=input().split()
    n=int(n)
    result=""
    if name=="Alice":
        if n%3==1: result="Bob"
        else: result="Alice"
    else:
        result="Bob" if n%3 else "Alice"
    print(f"Case {fi+1}: {result}")