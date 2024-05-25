from bs4 import BeautifulSoup
import requests as req

response = req.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

# Print the entire webpage content for debugging
# print(soup.prettify())

article_tags = soup.select("span.titleline a")

if article_tags:
    for article in article_tags:
        print(article.getText())
else:
    print("No elements found with the specified selector.")