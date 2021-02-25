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

from flask import Flask, jsonify

logo_list = []
for l in data_list:
    lg = {}
    lg['logos'] = "https://theinternship.io/" + l.logo
    logo_list.append(lg)

app = Flask(__name__)

@app.route('/company')
def index():
    data = {
        "company" : logo_list
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

#run the API request on http://localhost:5000/company