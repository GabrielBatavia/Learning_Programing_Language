import os
import tkinter as tk
from tkinter import ttk
import webview
import threading
from flask import Flask, render_template_string
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Spotify token from environment variable
token = os.getenv('SPOTIFY_TOKEN')

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    playlist_id = '4ZJOMIPy9JIPfZ9EUall55'
    iframe_code = f'''
    <iframe
      title="Spotify Embed: Recommendation Playlist "
      src="https://open.spotify.com/embed/playlist/{playlist_id}?utm_source=generator&theme=0"
      width="100%"
      height="100%"
      style="min-height: 360px;"
      frameborder="0"
      allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
      loading="lazy"
    ></iframe>
    '''
    return render_template_string(iframe_code)

def start_flask_app():
    app.run()

# Start Flask app in a separate thread
flask_thread = threading.Thread(target=start_flask_app)
flask_thread.daemon = True
flask_thread.start()

# Create Tkinter window
root = tk.Tk()
root.title("Spotify Playlist")
root.geometry("800x600")

# Create a webview window in Tkinter
webview.create_window("Spotify Playlist", "http://127.0.0.1:5000/", width=800, height=600)

# Start the webview and Tkinter event loop
webview.start()
root.mainloop()
