from tkinter import *
import requests
import json 
import sqlite3
import datetime
import time

root =Tk()

def show():
    Records=Tk()
    Records.title="Records"
    Records.geometry("400x400")
    conn=sqlite3.connect('weather_report.db')
    c=conn.cursor()
    c.execute("SELECT * , oid FROM weathers")
    records = c.fetchall()
    print(records)
    conn.commit()
    conn.close()
    Label(Records,text="Records",font="BigJohn 22",justify=CENTER).grid(row=0,column=0,columnspan=4,pady=20,sticky=(W+E))
    l1=Label(Records,text="City").grid(row=1,column=0,ipadx=15)
    l2=Label(Records,text="Country").grid(row=1,column=1,padx=5)
    l3=Label(Records,text="Temprature").grid(row=1,column=2,padx=10)
    l4=Label(Records,text="Date & Time").grid(row=1,column=3,padx=5)
    rows,columns=int(1),int(0)
    for record in records:
        for _ in range(3):
            city_label=Label(Records,text=record[0],borderwidth=3).grid(row=(rows+1),column= columns,padx=10)
            country_label=Label(Records,text=record[1]).grid(row=(rows+1),column= (columns+1),padx=5)
            temp_label=Label(Records,text=record[2]).grid(row=(rows+1),column= (columns+2),padx=10)
            date_label=Label(Records,text=record[3]).grid(row=(rows+1),column= (columns+3),padx=5)
        rows+=1


# conn=sqlite3.connect('weather_report.db')
# c=conn.cursor()
# c.execute("""CREATE TABLE weathers(

#                     city_name text,
#                     country_name text,
#                     temprature integer,
#                     time_record text
#           )""")
# conn.commit()
# conn.close()



def getreport():
        url="https://community-open-weather-map.p.rapidapi.com/weather"
        header={
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key' : "29f642b8femsh9de8386b831d195p1154a3jsn65db2443ceb7"
        }
        city=cityname.get().capitalize()
        country_name=country.get().capitalize()
        formt=city+","+country_name
        query={'q':"Lucknow,india"}
        query['q']=formt
        attime=time.strftime("%d/%A,%Y  %I:%M %p")
        try:
            api_response=requests.request("GET",url=url,params=query,headers=header)
            print(api_response.text)
            print(api_response.status_code)
            if api_response.status_code ==404:
                myweather.set("City Not found")
            else:
                api=json.loads(api_response.content)
                Name=api["name"]
                temp=api["main"]["temp"]
                temp_cel=round((temp-273.15),2)
                myweather.set(f"{Name} {temp_cel}C")
                if temp_cel>=22:
                    root.config(bg="green")
                conn=sqlite3.connect('weather_report.db')
                c=conn.cursor()
                c.execute("INSERT INTO  weathers VALUES(:city,:country,:temprature,:time_record)",
                                {
                                    'city':Name,
                                    'country':country_name,
                                    'temprature':temp_cel,
                                    'time_record': attime
                                })
                conn.commit()
                conn.close()
        except Exception as e:
            print(e)
    
global cityname
global country
global myweather
global ans_label

root.title("uWeather")

cityname=StringVar()
cityname.set("Gorakhpur")
myweather=StringVar()
country=StringVar()

Heading=Label(root,text=" Search for Weather Report").grid(row=0,column=0,columnspan=2)
Cityscreen=Entry(root,textvariable=cityname,width=30,background="skyblue").grid(row=1,column=1,pady=10)
Citylabel=Label(root,text="City Name").grid(row=1,column=0,padx=30)
Countryscreen=Entry(root,textvariable=country,width=30,background="skyblue").grid(row=2,column=1,pady=10)
Countrylabel=Label(root,text="Country Name").grid(row=2,column=0,padx=30)
get_report=Button(root,text="Get Report",command=getreport).grid(row=3,column=0,columnspan=2)
ans_label=Label(root,font="Algeria 20 bold",textvariable=myweather).grid(row=5,column=0 ,columnspan=2,pady=20)
show_rec=Button(root,text="Show records",command=lambda: show()).grid(row=4,column=0,columnspan=2,pady=10)
root.mainloop()