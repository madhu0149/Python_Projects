import requests
import json
import win32com.client as wincom

city = input('Enter the name of the city :\n')
url = f'https://api.weatherapi.com/v1/current.json?key=a8dbeac7ec984f0c961100251230204&q={city}'

r = requests.get(url)
print(r.text)
dic = json.loads(r.text)
print(dic["current"]['temp_f'])

speak = wincom.Dispatch("SAPI.SpVoice")
text = f"The current temperature in {city} is {dic['current']['temp_f']} fahrenheit"
speak.Speak(text)