import sys

sys.path.append('/Users/okazaki/.pyenv/versions/3.8.5/lib/python3.8/site-packages')


import datetime
import requests
import json
import schedule
from time import sleep
import chromedriver_binary
from selenium import webdriver
import time




# Payload: Search Criteria
limit = 1
# Minimum seismic intensity threshold. 10 (Intensity 1), 20 (Intensity 2), 30 (Intensity 3), 40 (Intensity 4), 45 (Intensity 5 lower), 50 (Intensity 5 upper), 55 (Intensity 6 lower), 60 (Intensity 6 upper), 70 (Intensity 7).
min_scale = 30


def earthquake_execute():
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    print(now)
    seconds_ago = now - datetime.timedelta(seconds=30)
    base_time = seconds_ago.strftime('%Y/%m/%d %H:%M:%S')
    print(base_time)




    # Extract earthquake information: Summary
    print(1)
    url = "https://api.p2pquake.net/v2/jma/quake"
    payload = {"limit":limit, "min_scale":min_scale}
    r = requests.get(url, params=payload)
    data = json.loads(r.text)
    print(2)

    # Extract earthquake information: Details
    info_url = url + '/' + data[0]['id']
    print(3)
    info_r = requests.get(info_url)
    print(4)
    info_data = json.loads(info_r.text)
    print(5)
    # Earthquake occurrence time
    quake_time = info_data['earthquake']['time']
    print(6)
    #quake_time = "2023/11/03 20:45:59"

    if quake_time>base_time:
        # Location of occurrence
        name = info_data['earthquake']['hypocenter']['name']
        # Maximum seismic intensity
        maxscale = info_data['earthquake']['maxScale']
        # Magnitude
        magnitude = info_data['earthquake']['hypocenter']['magnitude']

        #quake_time="2022/04/25 19:13:00"


        # Intensity classification
        if maxscale < 10:
            intensity = 'Less than 1'
        elif maxscale < 11:
            intensity = '1'
        elif maxscale < 21:
            intensity = '2'
        elif maxscale < 31:
            intensity = '3'
        elif maxscale < 41:
            intensity = '4'
        elif maxscale < 46:
            intensity = '5 lower'
        elif maxscale < 51:
            intensity = '5 upper'
        elif maxscale < 56:
            intensity = '6 lower'
        elif maxscale < 61:
            intensity = '6 upper'
        elif maxscale < 71:
            intensity = '7'


        # Output prefectures corresponding to (min_scale) or higher
        region = []

        for i in info_data['points']:
            if i['scale'] >= min_scale:
                region.append(i['pref'])

        # Process duplicate prefectures into one
        region = list(dict.fromkeys(region))
        str_region = "\n".join(region)

        # def send_message():

    
        headers = {
            'Authorization': 'Bearer YourLineNotifyToken',
        }

        messagefile="Emergency Earthquake Alert"+"======================="+"Occurrence Time:\n"+str(quake_time)+"\nEpicenter:"+name+"\nEstimated Maximum Intensity :"+intensity+"\nMagnitude:"+str(magnitude)
        
        files = {
            'message': (None,messagefile)
            

        }

        requests.post('https://notify-api.line.me/api/notify', headers=headers, files=files)

        # def send_picture():
        driver = webdriver.Chrome()
        driver.get("http://www.kmoni.bosai.go.jp")
        time.sleep(1)
        driver.set_window_size(500,900)
        #driver.get("https://typhoon.yahoo.co.jp/weather/jp/earthquake/kyoshin/")
        driver.save_screenshot("aaa.png")
        #driver.save_screenshot("")
        headers = {
            'Authorization': 'Bearer YourLineNotifyToken',
        }

        image = 'aaa.png'
        files = {
            'message': (None, 'Epicenter Information'),
            'imageFile': open(image, 'rb')
            #'stickerPackageId': 1, #Input sticker package ID 
            #'stickerId': 13, #Input sticker ID 
        }

        requests.post('https://notify-api.line.me/api/notify', headers=headers, files=files)

    else:
        print("Nothing")

    # if quake_time>base_time:
    #     print("An earthquake has occurred")
    #     send_message()
    #     send_picture()
    # else:
    #     print("Nothing happened")
    #     send_message()
    #     send_picture()


# earthquake_execute()

while True:
    earthquake_execute()
