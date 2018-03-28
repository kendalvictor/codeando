l=[2,-1,3,1,-2,-6]

l2=[x for x in l if x>0]
# es como en primaria: conjuntos por comprension
#l2=[x tal que x pertence a l :x > 0 ]
print l
print l2

l3=[x**2 for x in l if x>0]
print l3

s=['G','O','L']
s1=[x*y for x in l
            for y in s
                if x>0]
s2=[x*y for y in s
            for x in l
                if x>0]
#s3=[x*y for x in l]


print s
print s1
print s2
            
