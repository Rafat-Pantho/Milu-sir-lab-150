n= int(input())
a=[input() for i in range(n)]

count_of_co =0
row_count =[0]*n
col_count =[0]*n

for row in range (n):
    for col in range (n):
        if a[row][col]=='C':
            row_count[row]+=1
            col_count[col]+=1

for i in range(n):
    if row_count[i]>1:
        count_of_co+=((row_count[i]*(row_count[i]-1))//2)
    if col_count[i]>1:
        count_of_co+=((col_count[i]*(col_count[i]-1))//2)

print(count_of_co)