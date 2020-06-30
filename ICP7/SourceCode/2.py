from bs4 import BeautifulSoup
import urllib.request

url = "https://en.wikipedia.org/wiki/Google"
source_code = urllib.request.urlopen(url)
soup = BeautifulSoup(source_code, "html.parser")
body = soup.find('div', {'class': 'mw-parser-output'})

file = open('input.txt', 'a+', encoding='utf-8')
file.write(str(body.text))
print("File created")






