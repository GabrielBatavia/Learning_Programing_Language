import requests as req
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = req.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# Find all movie title elements
title_elements = soup.find_all(name="h3", class_="title")

# Extract and print the first 100 movie titles
movie_titles = [title.get_text() for title in title_elements[:100]]

# Since the titles are numbered from 100 to 1, we reverse the list to print them in the correct order
movie_titles.reverse()

with open("./S100_movies_to_watch/movie_list.txt", mode="w", encoding="utf-8") as file: 
    for title in movie_titles:
        file.write(f'{title}\n')
    