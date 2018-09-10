from bs4 import BeautifulSoup
import  requests


link = "https://www.digikala.com/search/?q=xbox&sortby=4";
r = requests.get(link)
data = r.content;

soup = BeautifulSoup(data);

xboxs_name = soup.select(".c-product-box__title a");
xboxs_price = soup.select(".c-price__value");
for price, name in zip(xboxs_price,xboxs_name):
    if("Xbox" in name.text):
        print(name.text + "  : "  + price.text);

