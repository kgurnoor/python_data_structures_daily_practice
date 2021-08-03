# cook your dish here
t= int(input())
for ty in range(t):
    w1,w2,x1,x2,m=[int(x) for x in input().split()]
    
    minn = w1+(x1*m)
    maxn= w1+(x2*m)
    if w2 > minn and w2<maxn :
        print("1")
    else:
        print("0")
    
   