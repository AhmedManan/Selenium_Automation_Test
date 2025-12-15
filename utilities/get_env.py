import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("DEMOBLAZE_USERNAME")
password = os.getenv("DEMOBLAZE_PASSWORD")
base_url = os.getenv("DEMOBLAZE_URL")