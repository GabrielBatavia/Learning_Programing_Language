from bs4 import BeautifulSoup

with open("./website.html", encoding='utf-8') as html:
    content = html.read()

soup = BeautifulSoup(content, 'html.parser')

#print(soup.title.name)
#print(soup.title.string)
#print()
#print(soup.prettify())

# to search something
#all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

#all_paragraphs = soup.find_all(name="p")
#print(all_paragraphs)

# get only the text
#for tag in all_anchor_tags:
#    print(tag.getText())


# get only the link in achor tag
#for tag in all_anchor_tags:
#    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# select really spesific item
# selector = "p a" means find link in anchor that in paragraph and it will print the first item that the program find
company_url = soup.select_one(selector="p a")
print(company_url)

# search id (id is using #)
name = soup.select_one(selector="#name")
print(name)

# get list of our heading tags
headings = soup.select(".heading")
print(headings)