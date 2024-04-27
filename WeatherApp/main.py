import requests
from PIL import ImageTk
from PIL import Image
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

font1 = ("Arial", 20, "bold")
font2 = ("Arial", 18, "bold")
font3 = ("Arial", 14, "bold")
app = tk.Tk()
app.title("Weather App")
app.geometry("1000x650")
app.configure(background="lightblue")


def get_weather(city):
    api_key = "2f1622e6b49ff98379fd81d4e10f4b48"
    city = city_entry.get()
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(url)

    if response.status_code == 404:
        messagebox.showerror("Error", "City could not be found")

    weather = response.json()
    icon_id = weather['weather'][0]['icon']
    temp_kelvin = weather['main']['temp']
    temp_celsius, temp_farenheit = convert_kelvin(temp_kelvin)
    feel_temp_kelvin = weather['main']['feels_like']
    feel_temp_celsius, feel_temp_farenheit = convert_kelvin(feel_temp_kelvin)
    city = weather['name']
    humidity = weather['main']['humidity']
    description = weather['weather'][0]['description']
    sunrise_time = datetime.fromtimestamp(weather['sys']['sunrise'] + weather['timezone'])
    sunset_time = datetime.fromtimestamp(weather['sys']['sunset'] + weather['timezone'])
    wind_speed = weather['wind']['speed']
    coord_longitutde = weather['coord']['lon']
    coord_latitude = weather['coord']['lat']
    pressure = weather['main']['pressure']
    min_temp_kelvin = weather['main']['temp_min']
    min_temp_celcius, min_temp_farenheit = convert_kelvin(min_temp_kelvin)
    max_temp_kelvin = weather['main']['temp_max']
    max_temp_celcius, max_temp_farenheit = convert_kelvin(max_temp_kelvin)
    visibility = weather['visibility']
    wind_speed = weather['wind']['speed']
    cloud_coverage = weather['clouds']['all']
    local_time = datetime.fromtimestamp(weather['dt'])
    timezone = weather['timezone']
    time = local_time + timedelta(seconds=timezone)
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temp_celsius, temp_farenheit, feel_temp_celsius,
            feel_temp_farenheit, humidity, sunrise_time, sunset_time,
            wind_speed, description, city, coord_longitutde,
            coord_latitude, pressure, min_temp_celcius, min_temp_farenheit,
            max_temp_celcius, max_temp_farenheit, visibility, wind_speed,
            cloud_coverage, time)


def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    icon_url, temp_celsius, temp_farenheit, feel_temp_celsius, feel_temp_farenheit, humidity, sunrise_time, sunset_time, wind_speed, description, city, coord_longitutde, coord_latitude, pressure, min_temp_celcius, min_temp_farenheit, max_temp_celcius, max_temp_farenheit, visibility, wind_speed, cloud_coverage, time = result
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon
    location_label.configure(text=f"City: {city}")
    coordinants_label.configure(text=f"Lon:{coord_longitutde} Lat:{coord_latitude}")
    temperature_label.configure(text=f"{temp_celsius}⁰C / {temp_farenheit}⁰F")
    feels_like_label.configure(text=f"Feels like:   {feel_temp_celsius}⁰C / {feel_temp_farenheit}⁰F")
    description_label.configure(text=f"{description}")
    humidity_label.configure(text=f"Humidity: {humidity}%")
    sunrise_label.configure(text=f"Sunrise: {sunrise_time}")
    sunset_label.configure(text=f"Sunset: {sunset_time}")
    pressure_label.configure(text=f"Pressure: {pressure}")
    min_temp_label.configure(text=f"Min temp: {min_temp_celcius}⁰C / {min_temp_farenheit}⁰F")
    max_temp_label.configure(text=f"Max temp: {max_temp_celcius}⁰C / {max_temp_farenheit}⁰F")
    visibility_label.configure(text=f"Visibility: {visibility}km")
    wind_speed_label.configure(text=f"Wind speed: {wind_speed}m/s")
    cloud_coverage_label.configure(text=f"Cloud coverage: {cloud_coverage}%")
    local_time_label.configure(text=f"Local time: {time}")


def convert_kelvin(kelvin):
    celcius = round(kelvin - 273.15)
    farenheit = round(celcius * (9/5) + 32)
    return celcius, farenheit


# Search bar
city_entry = tk.Entry(app, font=("Arial, 20"), background="grey", width=30)
city_entry.grid(row=0, column=0, pady=10, padx=50)
# Search button
search_button = tk.Button(app, command=search, text="⌕", font=("Arial, 20"))
search_button.grid(row=0, column=1, pady=5, padx=5)
# Location label
location_label = tk.Label(app, font=font1, background="lightblue")
location_label.grid(row=1, column=0, pady=5, padx=5)
# Coordinants
coordinants_label = tk.Label(app, font=font3, background="lightblue")
coordinants_label.grid(row=2, column=0, pady=5, padx=5)
# Local time
local_time_label = tk.Label(app, font=font3, background="lightblue")
local_time_label.grid(row=2, column=1, pady=5, padx=5)
# Weather icon
icon_label = tk.Label(app, background="lightblue")
icon_label.grid(row=3, column=0, pady=5, padx=5)
# Temperature widget
temperature_label = tk.Label(app, font=font1, fg="#7CFC00", background="lightblue")
temperature_label.grid(row=4, column=0, pady=10, padx=10)
# Feels like temperature
feels_like_label = tk.Label(app, font=font1, fg="#7CFC00", background="lightblue")
feels_like_label.grid(row=4, column=1, pady=10, padx=10)
# Minimum temperature
min_temp_label = tk.Label(app, font=font2, fg="#7CFC00", background="lightblue")
min_temp_label.grid(row=5, column=0, pady=10, padx=10)
# Maximum temperature
max_temp_label = tk.Label(app, font=font2, fg="#7CFC00", background="lightblue")
max_temp_label.grid(row=5, column=1, pady=10, padx=10)
# Description
description_label = tk.Label(app, font=font2, fg="#7CFC00", background="lightblue")
description_label.grid(row=3, column=1, pady=10, padx=10)
# Humidity
humidity_label = tk.Label(app, font=font2, background="lightblue")
humidity_label.grid(row=6, column=0, pady=10, padx=10)
# Pressure
pressure_label = tk.Label(app, font=font2, background="lightblue")
pressure_label.grid(row=6, column=1, pady=10, padx=10)
# Sunrise
sunrise_label = tk.Label(app, font=font2, background="lightblue")
sunrise_label.grid(row=7, column=0, pady=10, padx=10)
# Sunrise
sunset_label = tk.Label(app, font=font2, background="lightblue")
sunset_label.grid(row=7, column=1, pady=10, padx=10)
# Visibility
visibility_label = tk.Label(app, font=font2, background="lightblue")
visibility_label.grid(row=9, column=0, pady=10, padx=10)
# Cloud Coverage
cloud_coverage_label = tk.Label(app, font=font2, background="lightblue")
cloud_coverage_label.grid(row=9, column=1, pady=10, padx=10)
# Wind speed
wind_speed_label = tk.Label(app, font=font2, background="lightblue")
wind_speed_label.grid(row=10, column=0, pady=10, padx=10)

app.mainloop()
