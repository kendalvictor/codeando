import urllib3, certifi
import json
'''
Clave API:  c08cf1dcdcebec69c09c0870564fda430df00350
Identificador: upcencuestafinal
####################################################
User: alfred.kobayashi@upc.edu.pe
Pass: d1ns2k15
'''
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
UID='OrII55'#'ONHcwn'#'Hspihn'
CLAVE_API='c08cf1dcdcebec69c09c0870564fda430df00350'
desde = "/v0/form/"+UID+"?key="+CLAVE_API+"&completed=true"
r = http.urlopen('GET', 'https://api.typeform.com'+desde, preload_content=False)
data = r.read()
#print data
print "------------------------------------------------------------------------------"
#Decoded
decoded = json.loads(data)
#print 'DECODED:', decoded,'\n\n'

print "###################################################################################"
print "tama�o de data = "+ str(len(decoded)),'--------',str(type(decoded))
for key,value in decoded.items():
    print key,'--------',type(value)
    print value
    print ""
print "###################################################################################"

for key,value in decoded.items():
    if key=="questions":
        list_preguntas=value
        PREGUNTAS=value
        print "QUESTIONS: ",type(value)
        for x in value:
            print type(x),"//////////////////////////////////////////////////////////////////////////"
            for k,v in x.items():
                print k,"-----",v,"------",type(v),"\n"
            print ""
       
    if key=="responses":
        print "RESPONSES: ",type(value)
        list_dict_respuestas=[]
        for x in value:
            print type(x),"//////////////////////////////////////////////////////////////////////////"
            for k,v in x.items():
                if k=="answers":
                    list_dict_respuestas.append(v)
                if not k=="metadata":
                    print k,"-----",v,"------",type(v),"\n"
                else:
                    print "METADATA : ",type(v)
                    for k1,v1 in v.items():
                        print k1,"-----",v1,"------",type(v1),"\n"
                        
        print ""

print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print list_preguntas
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print list_dict_respuestas





    
    
