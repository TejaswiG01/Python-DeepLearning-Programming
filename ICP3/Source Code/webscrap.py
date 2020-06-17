import requests
from bs4 import BeautifulSoup

links = []
# Extracting the wiki page
wikiPage = requests.get("https://en.wikipedia.org/wiki/Deep_learning")

# parsing the wiki page content with BeautifulSoup library
data = BeautifulSoup(wikiPage.content, "html.parser")

# Printing the title of the page
print("Title of the Web Page: ", data.title.string)

# finding all the anchor tags and iterating over them
for link in data.find_all('a'):
    # getting the href of the link
    links.append(link.get('href'))
print("All the links in the page :" + str(links))

# Saving all the links to
with open('Output.txt', 'w') as file:
    for link in links:
        file.write('%s\n' % link)
