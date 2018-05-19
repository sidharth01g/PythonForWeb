import requests
from bs4 import BeautifulSoup

request = requests.get('https://www.reebok.com/us/reebok-crossfit-nano-2.0/CN7124.html')
# print(request)
# print(request.content)
# <span class="price-big gl-price">$110</span>
with open("shopping.html", 'w') as outfile:
    outfile.writelines(str(request.content))


soup = BeautifulSoup(request.content, "html.parser")
# print(soup)

element = soup.find(name="span", attrs={"class": "price-big gl-price"})
print(element)
print(element.text.strip())