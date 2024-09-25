n= int(input())
n-=2
arr1 = list(map(int,input().split()))
arr1.sort()
arr2=[]
for i in range(len(arr1)-1):
    count_same=0
    if arr1[-1]%arr1[i]!=0:arr2.append(arr1[i])
    if arr1[-1]%arr1[i]==0 and arr1[i]==arr1[i+1]:arr2.append(arr1[i])
print(arr1[-1], arr2[-1])