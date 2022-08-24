from urllib.request import urlopen
import json


def get_ip_data():
    url = 'https://ipinfo.io/json'
    response = urlopen(url)
    return json.load(response)


def get_all_data():
    data = get_ip_data()
    ip = data['ip']
    city = data['city']
    region = data['country']
    country = data['country']
    latitude = data['loc'].split(',')[0]
    longtitude = data['loc'].split(',')[1]
    return f'''IP-adress:  {ip}
City:  {city}
Region:  {region}
Country:  {country}
Latitude:  {latitude}
Longtitude:  {longtitude}'''
