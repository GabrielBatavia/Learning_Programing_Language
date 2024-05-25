from bs4 import BeautifulSoup

with open("./website.html", encoding='utf-8') as html:
    content = html.read()

soup = BeautifulSoup(content, 'html.parser')
print(soup.title.name)
print(soup.title.string)
print()

print(soup.prettify())