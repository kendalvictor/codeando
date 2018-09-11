import requests
from bs4 import BeautifulSoup
import re

headers = {
    'Authorization': "Basic YWRtaW46YWRtaW4=",
    'Cache-Control': "no-cache",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}

countrys_select = ['Austria', 'Italy', 'Belgium', 'Latvia', 'Bulgaria',
                  'Lithuania', 'Croatia', 'Luxembourg', 'Cyprus', 'Malta',
                  'Czech', 'Republic Netherlands', 'Denmark', 'Sweden', 'Ireland',
                  'Poland', 'Estonia',	'Portugal', 'Finland', 'Romania',
                  'France',	'Slovakia', 'Germany',	'Slovenia', 'Greece',
                  'Spain', 'Hungary', 'United Kingdom', 'Czech Republic',
                   'Netherlands', 'Slovak Republic', 'Republic of Lithuania']

domain = 'http://www.gatherproxy.com'
path_proxy_country = '/proxylistbycountry'
url_analysis_ip = "https://geoapi.eclabs.io/location/{}"


def apply_soup(domian, path):
    url = domain + path
    page = requests.get(url)
    soup = None
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        page.close()
    return soup


def get_analysis_ip(url, ip_country):

    dicc = \
        requests.request("GET", url.format(ip_country), headers=headers).json()

    return dicc.get('is_in_european_union', '-'),\
        'CORRECTO' if dicc.get('is_in_european_union', '-') == '1' else 'NIL',\
        dicc.get('organization', '-') + \
        ' ' + str(dicc.get('latitude', '-')) + \
        ' ' + str(dicc.get('longitude', '-')) + \
        ' ' + dicc.get('timezone', '-')


soup = apply_soup(domain, path_proxy_country)
for li in soup.find('ul', {"class": "pc-list"}).find_all('li'):
    new_path = li.find('a').attrs.get('href', '')

    country = new_path.split('?c=')[-1]
    if country not in countrys_select:
        continue

    print("///////////////////////", new_path.split('?c=')[-1])
    new_soup = apply_soup(domain, new_path)
    list_proxy = [
        tr.text.replace('gp.insertPrx(', '').replace(');', '')
        for tr in new_soup.find_all('script') if 'gp.insertPrx' in tr.text
    ][:10]

    for _ in list_proxy:
        transform = _.strip()
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', transform)[0]
        try:
            print(ip, '::::', get_analysis_ip(url_analysis_ip, ip))
        except Exception as e:
            print('error :: ', str(e))







