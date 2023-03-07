from tkinter import *
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime
import requests

def getweather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)


        home = pytz.timezone(result)
        local_time = datetime.now(home)
        curr_time = local_time.strftime("%I:%M %p")
        clock.config(text=curr_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=229ddb6d078654ebe324c264f8689647"
        response = requests.get(api).json()
        condition = response['weather'][0]['main']
        description = response['weather'][0]['description']
        temp = int(response['main']['temp']-273.15)
        pressure = response['main']['pressure']
        humidity = response['main']['humidity']
        wind = response['wind']['speed']

        t.config(text=f"{temp}°")
        c.config(text=f"{condition} | FEEL LIKE {temp}°")

        w.config(text=wind)
        h.config(text=humidity)
        p.config(text=pressure)
        d.config(text=description)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Input")




window = Tk()
window.title("Weather Predictor")
window.geometry("900x500+300+200")
window.resizable(False, False)

#search box
Search_img = PhotoImage(file="Weather\search.png")
my_img = Label(image=Search_img)
my_img.place(x=20, y=15)

textfield = Entry(window, justify="center", width=17, font=("poppins",25,"bold"), border=0, fg= "white", bg="#404040")
textfield.place(x=50, y=35)
textfield.focus()

search_icon = PhotoImage(file="Weather\search_icon.png")
my_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg= "#404040", command=getweather)
my_icon.place(x=400, y=28)

#logo
logo_img = PhotoImage(file="Weather\logo.png")
my_logo = Label(image=logo_img, borderwidth=0)
my_logo.place(x=150, y=100)

#Bottom Box
frame_img = PhotoImage(file="Weather\layer.png")
my_frame = Label(image=frame_img)
my_frame.pack(padx=5, pady=5, side=BOTTOM)

#time
name = Label(window,font=("arial",15,'bold'))
name.place(x=30, y=100)
clock = Label(window, font=("Helvetica",20))
clock.place(x=30, y=130)

#label
label1 = Label(window, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(window, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(window, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(window, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial",70,'bold'),fg="#ee666d")
t.place(x=400,y=150)
c = Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w = Label(text="...", font=("arial",20,'bold'),bg= "#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial",20,'bold'),bg= "#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial",20,'bold'),bg= "#1ab5ef")
d.place(x=450, y=430)
p = Label(text="...", font=("arial",20,'bold'),bg= "#1ab5ef")
p.place(x=670, y=430)





window.mainloop()

