import os
from dotenv import load_dotenv
from unfollow import Unfollow

load_dotenv()

# Set up
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')


web = Unfollow()
web.login(email=EMAIL, password=PASSWORD)

