# -*- coding: utf-8 -*-
import urllib3, certifi
import json
from urllib3 import HTTPConnectionPool
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
print data
print "------------------------------------------------------------------------------"
#Decoded
decoded = json.loads(data)
#print 'DECODED:', decoded,'\n\n'
'''
print "###################################################################################"
print "tamaño de data = "+ str(len(decoded)),'--------',str(type(decoded))
for key,value in decoded.items():
    print key,'--------',type(value)
    print value
    print ""
print "###################################################################################"
'''

for key,value in decoded.items():
    if key=="questions":
        list_preguntas=value

    if key=="responses":
        print "RESPONSES: ",type(value)
        list_dict_respuestas=[]
        for x in value:
            print type(x),"//////////////////////////////////////////////////////////////////////////"
            for k,v in x.items():
                if k=="answers":
                    list_dict_respuestas.append(v)


print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print list_preguntas
print "QUESTIONS: "
for x in list_preguntas:
    print type(x),"//////////////////////////////////////////////////////////////////////////"
    for k,v in x.items():
        print k,"-----",v,"------",type(v)
        print ""
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
print list_dict_respuestas

