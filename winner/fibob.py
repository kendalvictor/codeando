def fibonaci(n):
    a=0
    b=1
    for i in xrange(2,n):
        b=a+b
        a=b-a
        yield b

n=input('ingrese orden :')
print '0 1',
for x in fibonaci(n):
    print x,
