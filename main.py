import requests
import os
bot_token=os.environ.get("TELEGRAM_BOT_TOKEN")
chat_id=os.environ.get("TELEGRAM_CHAT_ID")
weather_api_key=os.environ.get("WEATHER_API_KEY")
parameters={
    "lat":38.9098,
    "lon":16.5877,
    "appid":weather_api_key,
    "cnt":4
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
# print(response.status_code)
print(response.json())
data_weather=response.json()
condition_list=[]
for status in data_weather["list"]:
    condition_list.append(status["weather"][0]["id"])
print(condition_list)
is_gonna_rain=False
for i in condition_list:
    if i< 700:
        is_gonna_rain=True
if is_gonna_rain:
    message="🌧️☂️Bring an Umbrella it's gonna rain today!"
else:
    message="There is no rain today!"

url=f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload={
        "chat_id": chat_id,
        "text": message
    }
telegram_message = requests.post(url=url, data=payload)
print(telegram_message.json())
telegram_message.raise_for_status()
print("Telegram message sent")

    # print("Bring an Umbrella")

# print(data_weather["list"][0]["weather"][0]["id"])
# print(data_weather["list"][0]["weather"][0]["description"])