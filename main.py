from forecast import get_hourly_forecast
from dotenv import load_dotenv
import requests
import os

load_dotenv()


def main():
    bot_token = os.getenv('TELEGRAM_TOKEN')
    bot_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    forecasts = get_hourly_forecast()

    for forecast in forecasts:
        if forecast.weather == 'Rain':
            message = f'{forecast.time}: It\'s going to rain! Make sure to bring an umbrella'
            url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' \
                  + bot_chat_id + '&parse_mode=Markdown&text=' + message

            response = requests.get(url)
            response.raise_for_status()
            break


if __name__ == '__main__':
    main()
