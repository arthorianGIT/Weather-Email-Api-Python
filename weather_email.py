import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv('.env')
api_key = os.getenv('api_key')