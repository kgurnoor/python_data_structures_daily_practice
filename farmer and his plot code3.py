# cook your dish here
def hcf(n,m):
    if n>m :
        smaller = m
    else :
        smaller = n 
    for i in range(1,smaller+1):
        if((n % i == 0) and (m % i == 0)): 
            hcfis=i 
    return hcfis
t=int(input())
for ty in range (t):
    n,m=[int(x) for x in input().split()]
    hcfis=hcf(n,m)
    
    no = int((n*m)/(hcfis*hcfis))
    print(no)
