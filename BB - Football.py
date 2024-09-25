n=input()
keep_count=1
max_keep=[]
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        keep_count+=1
    else:
        max_keep.append(keep_count)
        keep_count=1
max_keep.append(keep_count)
if max(max_keep)>=7: print("YES")
else: print("NO")