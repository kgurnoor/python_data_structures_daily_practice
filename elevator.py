# cook your dish here
t=int(input())
for ty in range(t):
    n, v1, v2=[int(pt) for pt in input().split()]
    t1=((2**(1/2))*n)/v1 
    t2=(2*n)/v2
    if t1<t2:
        print("Stairs")
    else:
        print("Elevator")