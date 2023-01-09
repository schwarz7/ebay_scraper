import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://www.ebay.com/itm/144432672459?hash=item21a0dbaecb:g:IR8AAOSwO6ZiReda&amdata=enc%3AAQAHAAAA8A5GrgEMZR%2BI6uZIgpxBRyV%2BTPSKSTRCRsJt%2B4BaIHQt8Gs%2BZx0M8%2FmuA0sgM%2Fk8njZyWE25XvX2PTqb4nec3FS%2BA6ScvNfo7iLtlNkuFK1YS1FvhsveEBEpKcBF%2BGUFo1raHlfEVF1NRjNGPRJ%2FAz7TxulQx9jYTk4UdZk9YqV1nwyEZcuXy1ExCrWlGA%2Fhrw0nzUHKwY38uIzNWexjFp2LBirNd0BD1OfVlIKOxVkPEiI4PBjXBvN820JvNJ%2FU7k%2FGYICYHTOWZu4FSilqT0RZf6dOq8aUDl1m600ZL2bcbslH7UgQ3Sew0EYAa5WGzg%3D%3D%7Ctkp%3ABFBMvPeV6rBh'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'} )
webpage = urlopen(req).read()
with requests.Session() as c:
	soup = BeautifulSoup(webpage, 'html5lib')
	price_dolar = float(soup.find('span', attrs= {'itemprop' : 'price'})['content'])
	price_real = soup.find('span', attrs= {'class' : "ux-textspans ux-textspans--SECONDARY ux-textspans--BOLD"}).get_text()
	price_real = price_real.replace('$','').replace('R','')
	price_real = price_real.replace(',', '.')
	price_real = price_real.split()
	price_real = price_real[0] + price_real[1]
	price_real = float(price_real)
	
	tax = price_real / price_dolar
	print(tax)


