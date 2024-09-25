for fi in range(int(input())):
    print(f"Case {fi+1}:")
    forwad=["http://www.lightoj.com/"]
    back=[]
    while True:
        command = input().split()
        if command[0]=="QUIT":
            break
        if visit