#Read the number of test cases.
t=int(input())
for ty in range(t):
    a,b=[int(x) for x in input().split()]
    p=a%b 
    print(p)