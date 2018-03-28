#Victor Villacorta 
from __future__ import print_function
noVacio=0
while noVacio==0:
    lin=raw_input()
    if len(lin)>0 and lin.isspace()==False:
        noVacio=1
        
TEXTO1=lin.split(" ")
TEXTO2=[]    
rastreo=0 
x=0 
for i in TEXTO1:
    try:
        TEXTO2.append(int(i))
        TEXTO1[x]=int(i)
        rastreo+=1
        x+=1
    except ValueError: 
        if i.islower():
            TEXTO2.append(i)
            x+=1
        
TEXTO2.sort() 
ORDEN=[]
s=0
t=rastreo
for j in TEXTO1:
    if isinstance(j,int):
        ORDEN.append(str(TEXTO2[s]))
        s=s+1
    elif isinstance(j,str):
        if j.islower():
            ORDEN.append(TEXTO2[t])
            t=t+1

for i in ORDEN:
    print(i, end=' ')

raw_input("\n\n\nPRESS ENTER TO EXIT....")
