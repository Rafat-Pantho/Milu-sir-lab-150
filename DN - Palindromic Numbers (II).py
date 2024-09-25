for fi in range(int(input())):
    s=input()
    print(f"Case {fi+1}: Yes" if s==s[::-1] else f"Case {fi+1}: No")