import requests
import datetime
key ="2e215d0a9a709fe8c21bca8822cd7754"


def get_data_json():
    url =f"https://api3.adsterratools.com/publisher/stats.json?start_date={datetime.date.today()}&finish_date={datetime.date.today()}&group_by=date"

    header = {
        "X-API-Key" : key
    }
    data = requests.get(url,headers=header)
    return data.json()


get_data_json()