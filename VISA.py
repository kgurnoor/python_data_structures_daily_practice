# cook your dish here
t=int(input())
for ty in range(t):
    x1, x2 ,y1,y2,z1,z2 = [int(x) for x in input().split()]
    if x1<=x2 and y1<=y2 and z1>=z2 :
        print("yes")
    else:
        print("no")