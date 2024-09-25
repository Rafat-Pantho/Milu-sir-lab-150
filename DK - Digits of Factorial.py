from math import log 
storage = [0]*1000001
storage[0]=0

for i in range(1,1000001):
    storage[i]=storage[i-1]+log(i)

for fi in range(int(input())):
    n,base=map(int,input().split())
    
    print(f"Case {fi+1}:",int(storage[n]/log(base))+1)