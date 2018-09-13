from bs4 import BeautifulSoup
import  requests
import re


link = "https://www.digikala.com/search/?q=xbox&sortby=4";
r = requests.get(link)
data = r.content;
m = re.findall(r'\d*', 'abcdef33212assada')
print("salam")
print(m)

soup = BeautifulSoup(data);
# file = open('prive-data', 'w')
xboxs_name = soup.select(".c-product-box__title a");
xboxs_price = soup.select(".c-price__value");
for price, name in zip(xboxs_price,xboxs_name):
    if("Xbox" in name.text):
        print(name.text + "  : "  + price.text);
        length = len(str(price.text).split(" "));
        print(str(price.text).split(" ")[60]);
        # print((re.findall(r'\d*',price)));
# file.close()
