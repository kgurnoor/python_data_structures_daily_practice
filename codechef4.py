# cook your dish here
l,r= [int(x) for x in input().split()]
if l%2==0:
    list1= [x for x in range(l+1,r+1,2)]
    
else :
    list1= [y for y in range(l,r+1,2)]

for p in list1 :
    print (p , end=" ")
    