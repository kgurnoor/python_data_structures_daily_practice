# cook your dish here
t=int(input())
for ty in range(t):
    n=int(input())
    hra= 10
    da=98
    if n<=1500:
        gross=n + ((10*n)/100)+ ((90*n)/100)
        print(gross)
    if n>=1500 :
        gross = n+ 500 +((98*n)/100)
        print(gross)