for i in range(int(input())):
    crnt_p_me,crnt_p_lift=map(int,input().split())
    print("Case "+str(i+1)+":",crnt_p_me*4+19+abs(crnt_p_me-crnt_p_lift)*4)