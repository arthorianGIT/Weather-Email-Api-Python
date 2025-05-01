import requests
import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText

load_dotenv('.env')
api_key = os.getenv('api_key')
my_email = os.getenv('my_email')
smtp_password = os.getenv('smtp_password')

def send_weather():
    global api_key
    global my_email
    params = {
        'q': input('City: '),
        'appid': api_key
    }
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    
    if response.status_code == 200:
        data = response.json()
        message = MIMEText(f'City: {data['name']}\nTemperature: {data['main']['temp'] - 273.15:.1f}°C\nWeather description: {data['weather'][0]['description'].title()}\nHumidity: {data['main']['humidity']}%')
        message['Subject'] = 'Weather info to you!'
        message['From'] = 'kirwl. who'
        message['To'] = my_email
        host = smtplib.SMTP(host='smtp.gmail.com', port=587)
        host.starttls()
        host.login(my_email, smtp_password)
        host.sendmail(my_email, message['To'], message.as_string())
        host.quit()
    else:
        print(f'Error: {response.status_code}')

send_weather()