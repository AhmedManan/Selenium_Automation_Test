import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("demoblaze_username")
password = os.getenv("demoblaze_password")