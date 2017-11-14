import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString


def equal_len(list1, list2):
    nn = list1.__len__() - list2.__len__()
    if nn > 0:
        for x in range(nn):
            list2.insert(0, "")


def find_tag(tag):
    return [x.get_text() for x in data.find_all(tag) if x.get_text().strip()]


API_url = 'http://www.corpac.gob.pe/app/Meteorologia/tiempo/consultas/select1.php'
response = requests.post(API_url, data={"aerop": "spme"})

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser').__iter__()
    for data in soup:
        if isinstance(data, NavigableString):
            pass
        else:
            th, td = find_tag("th"), find_tag("td")
            if th and td:
                equal_len(th, td)
                for campo, info in zip(th, td):
                    print(campo, ": ", info)
            th.clear()
            td.clear()
else:
    raise Exception(response.reason)


