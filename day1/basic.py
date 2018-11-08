import requests
from bs4 import BeautifulSoup

url = "https://www.biqukan.com/1_1094/5403177.html"
response = requests.get(url=url)
bf = BeautifulSoup(response.text, "html.parser")
content = bf.find_all("div", id="content")
print(content[0].text.replace("\xa0"*8, "\n\n"))