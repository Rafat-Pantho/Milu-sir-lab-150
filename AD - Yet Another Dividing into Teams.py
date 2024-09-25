for fi in range (int(input())):
    n= int(input())
    a= list(map(int,input().split()))
    a.sort()
    fin_of_the_fish = True
    for i in range (n-1):
        if a[i+1]-a[i]==1:
            fin_of_the_fish = False
            break
    print(1 if fin_of_the_fish else 2)