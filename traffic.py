from bs4 import BeautifulSoup
import  requests
import re
from PIL import Image
import urllib.request
import datetime


#marzdaran Highway
urllib.request.urlretrieve("http://31.24.237.150/TTCCTrafficWebSite/UploadedFiles/WebTrafficImages/Web102.png",
 str(datetime.datetime.now())+".png");
print("sal")
