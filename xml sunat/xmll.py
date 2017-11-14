from lxml import etree

ruta = "20338570041-03-B999-00013.xml"
xml = etree.parse(ruta, parser=etree.XMLParser(recover=True))

for datus in xml.iter():
	if isinstance(datus.tag, str):
		print(datus.tag.split("}")[1] , " -->  ", datus.text)
print("############")
print("############")
print("############")
del xml
