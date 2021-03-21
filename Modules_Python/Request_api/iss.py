import requests

try:
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    data= response.json()

    iss_pos = data['iss_position']
    print(iss_pos)

    print('status code: ',response.status_code)

except Exception as e:
    print(e)

