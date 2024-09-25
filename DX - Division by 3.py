def something(m):
    if m==0:return 0
    return m-((m//3)+1 if m%3 else m//3)
for fi in range(int(input())):
    a,b=map(int,input().split())
    print(f"Case {fi+1}:",something(b)-something(a-1))