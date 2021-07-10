# cook your dish here
t=int(input())
for m in range(t):
    a,b,c,d=[int(x)for x in input().split()]
    r = int(a+c) 
    u = int(b+d)
    if r==180 and u==180:
        print("YES")
    else:
        print("NO")