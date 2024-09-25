s=int(input())
l=s//100
r=s%100
if 1<=l<=12:print("AMBIGUOUS" if 1<=r<=12 else "MMYY")
else:print("YYMM" if 1<=r<=12 else "NA")