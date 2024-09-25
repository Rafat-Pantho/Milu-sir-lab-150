n= int(input())
arr1 = list(map(int,input().split()))
arr2 = []
count =1
for i in range(n-1):
    if arr1[i+1]>=arr1[i]:
        count+=1
    else:
        arr2.append(count)
        count=1
arr2.append(count)
print(max(arr2))