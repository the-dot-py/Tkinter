import json
import requests

def tocel(value):
    
    return (value-273.15)


url="https://community-open-weather-map.p.rapidapi.com/weather"
para={
'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
'x-rapidapi-key' : "29f642b8femsh9de8386b831d195p1154a3jsn65db2443ceb7"
}

entry=input("Enter city name")
query={'q':'Lucknow,india'}
query["q"]=entry






try:
    response=requests.request("GET",url,headers=para,params=query)
    # print(response.text,end="\n")
    status=(response.status_code)
    if status==404:
        print("City Not Found")
        exit()
    else:
        api=json.loads(response.content)
        Name=api["name"]
        mintemp=api["main"]["temp_min"]
        mintemp_cel=tocel(mintemp)
        print(Name,'%.2f'%mintemp_cel +u'\u00b0')
except Exception as e:
    print(e)