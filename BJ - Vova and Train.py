for fi in range(int(input())):
    L,v,l,r=map(int,input().split())
    print(int(L/v)-int(r/v)+int((l-1)/v))