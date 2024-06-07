import requests
from bs4 import BeautifulSoup

url = "https://stocktwits.com"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

messages = soup.find_all("div", class_="StreamMessage_main__qWCNf")
for message in messages:
  print(message)
