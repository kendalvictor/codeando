def primo(n):
    i=2
    while i<math.sqrt(n):
        if n%i==0:
            return False
        i+=1
    return True

import math
n=input('ingrese numero :')
if primo(n):
    print 'es primo'
else:
    print 'no es primo'
        

    
   
