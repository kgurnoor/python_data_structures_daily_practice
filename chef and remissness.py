# cook your dish here
t=int(input())
for ty in range(t):
    A,B=[int(x)for x in input().split()]
    minimum=max(A,B)
    maximum=A+B 
    print(minimum,  maximum)