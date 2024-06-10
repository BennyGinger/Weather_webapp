import dotenv
from os import getenv
import requests

dotenv.load_dotenv()
API = getenv("API_KEY")

def get_data(place: str, days: int):
    
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API}"
    response = requests.get(url)
    raw = response.json()
    # Filter data
    data = raw['list']
    # Filter by days of froecast
    days_idx = days * 8
    return data[:days_idx]
    # Filter by option
    # if option == 'Temperature':
    #     final_data = [round(x['main']['temp']/10,ndigits=1) for x in data]
    #     dates = [x['dt_txt'] for x in data]
    # elif option == 'Sky':
    #     final_data = [x['weather'][0]['main'] for x in data]
    #     dates = [x['dt_txt'] for x in data]
    # return dates, final_data

if __name__ == "__main__":
    data = get_data('London', 1)
    # dict_keys(['dt', 'main', 'weather', 'clouds', 'wind', 'visibility', 'pop', 'rain', 'sys', 'dt_txt'])
    print(data)