# cook your dish here
t=int(input())
for ty in range (t):
    x,y,z = [int(pq) for pq in input().split()]
    if x+y==z or y+z==x or x+z==y  :
        print("YES")
    else:
        print("NO")
