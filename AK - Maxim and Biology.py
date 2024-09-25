import math

n = int(input())
s = input()
max_operations = math.inf
for i in range(n - 3):
    new_s = s[i:i + 4]
    operations = 0
    for j in range(4):
        targ = "ACTG"
        operations += min(abs(ord(new_s[j]) - ord(targ[j])), 26 - abs(ord(new_s[j]) - ord(targ[j])))
    max_operations = min(operations, max_operations)
print(max_operations)
