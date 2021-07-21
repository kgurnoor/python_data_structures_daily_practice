# cook your dish here
t=int(input())
for ty in range(t):
    a,b,c,d= [int(x) for x in input().split()]
    if a==b and c==d:
        print("YES")
    elif b==c and a==d:
        print("YES")
    elif c==a and b==d:
        print("YES")
    else:
        print("NO")