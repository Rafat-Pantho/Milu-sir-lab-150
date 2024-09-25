n,m,r=map(int,input().split())
buying=list(map(int,input().split()))
selling=list(map(int,input().split()))
if min(buying)>=max(selling):
    print(r)
else:
    print(r%min(buying) + (r//min(buying))*max(selling))