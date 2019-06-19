import requests
from bs4 import BeautifulSoup

p = requests.get("https://4pda.ru")
soup = BeautifulSoup(p.content, "html.parser")
for i in soup:
    print(soup.find_all({"a":"title"}))