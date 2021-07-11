# cook your dish here
t=int(input())
for a in range(t):
    x,m,d = [int(p) for p in input().split()]
    s=x*m 
    q=x+d 
    print (min(q,s))
