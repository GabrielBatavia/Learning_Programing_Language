import requests as req
from bs4 import BeautifulSoup
URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

# Function to scrape song titles from a given Billboard Hot 100 URL
def scrape_song_titles(url):
    response = req.get(url)
    website_html = response.text

    soup = BeautifulSoup(website_html, "html.parser")

    # Finding the song title elements
    song_title_elements = soup.find_all("span", class_="chart-element__information__song")

    # Extracting the text (song titles) from the elements
    song_titles = [song.get_text() for song in song_title_elements]

    return song_titles


input("Which time you want to travel? Type the data in this format YYYY-MM-DD : ")

