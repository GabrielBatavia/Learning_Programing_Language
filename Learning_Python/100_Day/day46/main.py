import requests as req
from bs4 import BeautifulSoup

# Function to scrape song titles from a given Billboard Hot 100 URL
def scrape_song_titles(url):
    response = req.get(url)
    website_html = response.text

    soup = BeautifulSoup(website_html, "html.parser")

    # Finding the song title elements using the correct selector
    song_title_elements = soup.select("li.lrv-u-width-100p h3")

    # Extracting the text (song titles) from the elements
    song_titles = [song.get_text(strip=True) for song in song_title_elements]

    return song_titles

# Prompting the user for a date to travel
date = input("Which time you want to travel? Type the date in this format YYYY-MM-DD: ")

# Constructing the URL based on the user input date
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

# Scraping the song titles
song_titles = scrape_song_titles(URL)

# Printing the list of song titles
print("Song titles on Billboard Hot 100 for the selected date:")
for title in song_titles:
    print(title)
