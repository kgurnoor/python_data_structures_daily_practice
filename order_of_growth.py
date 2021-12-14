

def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

L = [1, 3, 4, 5, 9, 18, 27]
e=19
print(linear_search(L,e))
