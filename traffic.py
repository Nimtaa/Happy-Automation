from bs4 import BeautifulSoup
import  requests
import re
from PIL import Image




link = "http://31.24.237.150/TTCCTrafficWebSite/PublicUsers/GraphicalTrafficMap/Default.aspx";
r = requests.get(link)
data = r.content;

soup = BeautifulSoup(data);
file = open('marzdaran_square.jpg', 'w')
marzdaran_square = soup.select("#tdImage102");
image = Image.open(marzdaran_square)
image.show()

file.write(marzdaran_square);        # print((re.findall(r'\d*',price)));
file.close()
