import requests
from bs4 import BeautifulSoup

respuesta = requests.get('http://www.kitco.com/', headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
})
soup = BeautifulSoup(respuesta.content, 'html.parser')
low = soup.find(attrs={'id': 'AU-low'})
high = soup.find(attrs={'id': 'AU-high'})

print('Precio más bajo: {}'.format(low.text))
print('Precio más alto: {}'.format(high.text))

from re import search
