import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

#Opening connection, grabbing page
uClient = uReq(my_url)

#Loading into variable
page_html = uClient.read()

#Closing connection
uClient.close()

#Load into soup
pageSoup = soup(page_html, "html.parser")

containers = pageSoup.findAll("div", {"class":"item-container"})

for container in containers:
	brand = container.div.div.a.img["title"]

	titleContainer = container.findAll("a", {"class":"item-title"})
	productName = titleContainer[0].text

	shippingContainer = container.findAll("li", {"class": "price-ship"})
	shipping = shippingContainer[0].text.strip()

print("brand: " + brand)
print("productName: " + productName)
print("shipping: " + shipping)