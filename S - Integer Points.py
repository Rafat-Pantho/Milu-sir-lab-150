for fi in range (int(input())):
    m= int(input())
    p=[(int(i)%2) for i in input().split()]
    n=int(input())
    q=[(int(i)%2) for i in input().split()]
    
    even_p = p.count(0)
    odd_p = p.count(1)
    even_q = q.count(0)
    odd_q = q.count(1)
    count = ((even_p*even_q)+(odd_p*odd_q))
    print(count)