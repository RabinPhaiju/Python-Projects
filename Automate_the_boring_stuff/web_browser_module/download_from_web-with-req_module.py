import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
if not res.raise_for_status():
    with open('RomeoAndJuliet.txt','wb') as file:
        for chunk in res.iter_content(100000):
            file.write(chunk)