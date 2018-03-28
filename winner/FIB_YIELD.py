def fibonaci(n):
    a=0
    b=1
    for i in range(2,n):
        b=a+b
        a=b-a
        yield b

for x in fibonaci(5):
    print x,

