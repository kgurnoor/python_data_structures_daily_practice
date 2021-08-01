t=int(input())
for ty in range(t):
    m ,h= [int(x) for x in input().split()]
    bmi=(m/(h**2))
    if bmi<=18:
        print("1")
    if bmi>=19 and bmi<=24:
        print("2")
    if bmi>=25 and bmi<=29:
        print("3")
    
    if bmi>=30:
        print("4")