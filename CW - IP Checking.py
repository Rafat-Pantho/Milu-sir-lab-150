for fi in range(1,int(input())+1):
    x_dec=list(map(int,input().split(".")))
    x_bin=list(map(str,input().split(".")))
    x=False
    if x_dec[0]==int(x_bin[0],2) and x_dec[1]==int(x_bin[1],2) and x_dec[2]==int(x_bin[2],2) and x_dec[3]==int(x_bin[3],2):
        x=True
    print(f"Case {fi}: Yes" if x else f"Case {fi}: No")