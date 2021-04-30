import requests

parameter = {
    'lat':51.507351,
    'lng':-0.127758,
    'formatted':0
}

respones = requests.get('https://api.sunrise-sunset.org/json',params= parameter)

respones.raise_for_status()

data = respones.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

sunrise  = sunrise.split('T')
print(sunrise)