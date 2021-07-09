# cook your dish here
t=int(input())
for i in range(t):
    d,x,y,z= [int(x)for x in input().split()]
    s1 = int(7*x) 
    s2 = int((d*y)+((7-d)*z))
    if s1>s2:
        print(s1)
    else:
        print(s2)