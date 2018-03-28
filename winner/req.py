# -*- coding: utf-8 -*-
import requests
import json
'''
>>> r = requests.get(’https://api.github.com/user’, auth=(’user’, ’pass’))
>>> r.status_code
200
>>> r.headers[’content-type’]
’application/json; charset=utf8’
>>> r.encoding
’utf-8’
>>> r.text
u’{"type":"User"...’
>>> r.json()
{u’private_gists’: 419, u’total_private_repos’: 77, ...}

'''
UID='OrII55'#'ONHcwn'#'Hspihn'
CLAVE_API='c08cf1dcdcebec69c09c0870564fda430df00350'
desde = "/v0/form/"+UID+"?key="+CLAVE_API+"&completed=true"
r = requests.get('https://api.typeform.com' + desde)
print r.status_code
print r.headers
print r.encoding
data = r.text
#decoded = json.loads(data)
decoded = json.loads(r.content)
#print "Tenemos "+str(decoded["Fruteria"][1]["Verdura"][0]["Cantidad"])+" Lechugas."

preguntas=[]
dict={}
for i in range(0,len(decoded["questions"])):
    dict["id"]=decoded["questions"][i]["id"]
    dict["decoded"]=decoded["questions"][i]["question"]
    preguntas.append(dict)

print preguntas
print "/////////////---------------------------///////////////////"
for key,value in decoded.items():
    if key=="questions":
        list_preguntas=value

    if key=="responses":
        list_responses=value
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

#print "Tenemos "+str(decoded["Fruteria"][1]["Verdura"][0]["Cantidad"])+" Lechugas."
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"


