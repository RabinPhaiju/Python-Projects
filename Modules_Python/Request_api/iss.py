import requests
from datetime import datetime
import smtplib
import time

my_email = 'rabinphaiju@gmail.com'
password = 'kdslfkjdslf'

my_latlng = {
    'lat':27.671022,
    'lng':85.429817
}

while True:
    time.sleep(60)

    try:
        response = requests.get(url='http://api.open-notify.org/iss-now.json')
        data= response.json()

        iss_time = data['timestamp']
        iss_time = datetime.fromtimestamp(iss_time).isoformat().split('T')
        iss_pos = data['iss_position']
        iss_time = iss_time[1].split(':')[0]
    

        if (float(iss_pos['latitude'])-my_latlng['lat']) == 5 or (float(iss_pos['latitude'])-my_latlng['lat']) == -5:
            if (float(iss_pos['longitude'])-my_latlng['lng']) == 5 or (float(iss_pos['longitude'])-my_latlng['lng']) == -5:
                if iss_time>20 and iss_time<24:
                    with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
                        connection.starttls()
                        connection.login(user=my_email,password=password)
                        connection.sendmail(
                        from_addr=my_email,
                        to_addrs='lsdkhfl@gmail.com',
                        msg='Subject:iss over you\n\n Look at the sky'
        )

        # print('status code: ',response.status_code)

    except Exception as e:
        print(e)
