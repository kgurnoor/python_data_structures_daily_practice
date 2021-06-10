import re
fname = input('file name ?')
handle = open(fname)
sum = 0
count= 0
for line in handle :
    f=re.findall('[0-9]+', line)
    for num in f:
        if int(num)>0 :
            print(num)
            count = int(count+1)
            sum = sum+int(num)
print ('there are',count, 'values with a sum =', sum)
