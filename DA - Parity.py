for i in range(int(input())):
    print("Case "+str(i+1)+": odd" if (str(bin(int(input()))).replace("0b", "")).count('1')%2 else "Case "+str(i+1)+": even")