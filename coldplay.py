# cook your dish here
t=int(input())
for x in range(t):
    m,s = [int(i)for i in input().split()]
    ans=int(m/s)
    print(ans)