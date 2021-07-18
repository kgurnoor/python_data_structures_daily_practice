# cook your dish here
t=int(input())
for xy in range(t):
    q , p = [float(x) for x in input().split()]
    if q>1000 :
        discount=10
        expense= (q*p)-(q*p*discount/100)
        print(expense)
    else :
        expense=q*p 
        print(expense)