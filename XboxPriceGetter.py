from bs4 import BeautifulSoup
import  requests
link = "https://www.digikala.com/search/?q=xbox&sortby=4";
r = requests.get(link)
data = r.content;

soup = BeautifulSoup(data);

xboxs_name = soup.select(".c-product-box__title a");
xboxs_price = soup.select(".c-product-box__content");
for x in xboxs_price:
    if("Xbox" in x.text):
        print(x.text);

