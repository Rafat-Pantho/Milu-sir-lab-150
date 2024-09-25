for fi in range (int(input())):
    n=int(input())
    max_num = ""
    if n%2==0:
        max_num = "1"*(n//2)
    else:
        max_num = "7" + "1" * int((n-3)/2)
    print(max_num)