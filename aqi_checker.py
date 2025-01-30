from tkinter import *
from requests import get

# Initialize the main window
root = Tk()
root.title("Air Quality Index by Om")
root.geometry("750x650+300+40")

# Font style
f = ("Arial", 36, "bold")

# Function to clear the result labels
def clear_result():
    lab_api.configure(text="")
    lab_category.configure(text="")

# Function to fetch and display AQI
def fetch_aqi():
    clear_result()
    city = ent_city.get().strip()
    if not city:
        lab_api.configure(text="Please enter a city name", fg="red")
        return

    token = "cf0afdcbe485f3183580701610f309dfb356e651"
    url = f"https://api.waqi.info/feed/{city}/?token={token}"

    try:
        res = get(url)
        data = res.json()

        if data['status'] == 'ok':
            aqi = data['data']['aqi']
            category, color = get_aqi_category(aqi)
            lab_api.configure(text=f"AQI: {aqi}", fg=color)
            lab_category.configure(text=f"Category: {category}", fg=color)
        else:
            lab_api.configure(text="City not found", fg="red")
    except Exception as e:
        lab_api.configure(text="Error fetching data", fg="red")

# Function to determine AQI category and color
def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good", "green"
    elif aqi <= 100:
        return "Moderate", "yellow"
    elif aqi <= 150:
        return "Unhealthy for sensitive groups", "orange"
    elif aqi <= 200:
        return "Unhealthy", "red"
    elif aqi <= 300:
        return "Very unhealthy", "purple"
    else:
        return "Hazardous", "maroon"

# GUI Elements
lab_header = Label(root, text="Air Quality Index", font=f)
lab_city = Label(root, text="Enter City Name", font=f)
ent_city = Entry(root, font=f)
btn_generate = Button(root, text="Find AQI", font=f, command=fetch_aqi)
lab_api = Label(root, text="", font=f)
lab_category = Label(root, text="", font=f)

# Packing GUI Elements
lab_header.pack(pady=20)
lab_city.pack(pady=20)
ent_city.pack(pady=20)
btn_generate.pack(pady=20)
lab_api.pack(pady=20)
lab_category.pack(pady=20)

# Start the main loop
root.mainloop()