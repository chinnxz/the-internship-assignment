import requests
url = "https://theinternship.io/"
data = requests.get(url)
from bs4 import BeautifulSoup

class company:
    def __init__(self, logo, des):
        self.logo = logo
        self.des = des

data_list = []

soup = BeautifulSoup(data.text,'html.parser')
x = soup.find_all("img",{"class":"center-logos"})
y = soup.find_all("span",{"class":"list-company"})
k = 0

for i in x:
    st = str(i['src'])
    data_list.append(company(st, 0))

for j in y:
    num = len(j.text)
    data_list[k].des = num
    k = k + 1

data_list.sort(key = lambda x: x.des)

for obj in data_list: 
    print(obj.logo) 