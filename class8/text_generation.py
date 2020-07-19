import requests
from bs4 import BeautifulSoup

response = requests.get("http://gadyakosh.org/gk/%E0%A4%85%E0%A4%B2%E0%A4%97%E0%A5%8D%E0%A4%AF%E0%A5%8B%E0%A4%9D%E0%A4%BE_/_%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A5%87%E0%A4%AE%E0%A4%9A%E0%A4%82%E0%A4%A6")

soup = BeautifulSoup(response.text)
all_para = soup.find_all("p")
para_text = ".".join([para.get_text() for para in all_para])

print(response)

import pandas as pd
pd.read_csv