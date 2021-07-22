# cook your dish here
t=int(input())
for x in range(t):
    s = int(input())
    year=[2010,2015,2016,2017,2019]
    if s in year:
        print("HOSTED")
    else:
        print("NOT HOSTED")