def is_even(i):
    remainder=i%2
    return remainder==0

for i in range(20):
    if is_even(i) :
        print(i,"even")

    else:
        print(i,"odd")
