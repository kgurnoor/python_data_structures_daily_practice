
t=int(input())
for i in range(t):
    a,b,x = [int(x) for x in input().split()]
    ans = int((b-a)/x)
    print(ans)

