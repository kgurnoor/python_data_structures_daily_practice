def g(x):
    def h():
        x='abc'
    x=x+1
    print('g:x =',x)
    h()
    return x


x=3
z=g(x)    
