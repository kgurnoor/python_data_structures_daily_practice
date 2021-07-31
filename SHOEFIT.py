# cook your dish here
t=int(input())
for ty in range(t):
    
    
    a,b,c=[int(x) for x in input().split()]
    if (a==1 and (b==0 or c==0)):
        print("1")
    elif(a==0 and(b==1 or c==1)):
        print("1")
    else:
        print("0")

    