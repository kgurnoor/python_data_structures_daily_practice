# cook your dish here
t=int(input())
for i in range (t):
    
    xa,xb,Xa,Xb= [int(p) for p in input().split()]
    A=Xa/xa
    B=Xb/xb
    number=int(A+B)
    print(number)