# cook your dish here
t= int(input())
for x in range(t):
    
    a,b=[int(x) for x in input().split()]
    if a>b:
        print(">")
    if a<b:
        print("<")
    if a==b:
        print("=")