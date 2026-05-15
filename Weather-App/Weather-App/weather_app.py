from tkinter import *
from tkinter import messagebox
import requests

# ================= WINDOW =================

root = Tk()

root.title("Weather App")
root.geometry("500x700")
root.config(bg="#121212")
root.resizable(False, False)

# ================= API KEY =================

API_KEY = "e5dd91d8c989d8960bef12c78cfbdabd"

# ================= FUNCTION =================

def get_weather():

    city = city_entry.get()

    if city == "":
        messagebox.showerror(
            "Error",
            "Please enter city name!"
        )
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={API_KEY}&units=metric"
    )

    try:

        response = requests.get(url)
        data = response.json()

        if str(data["cod"]) != "200":

            messagebox.showerror(
                "Error",
                "City not found!"
            )
            return

        temp = data["main"]["temp"]
        weather = data["weather"][0]["main"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        city_label.config(
            text=f"{city.title()}"
        )

        temp_label.config(
            text=f"{temp}°C"
        )

        weather_label.config(
            text=f"{weather}"
        )

        details_label.config(
            text=f"Humidity: {humidity}%\nWind Speed: {wind} m/s"
        )

        # Weather Emoji
        if weather == "Clear":
            emoji_label.config(text="☀️")

        elif weather == "Clouds":
            emoji_label.config(text="☁️")

        elif weather == "Rain":
            emoji_label.config(text="🌧️")

        elif weather == "Thunderstorm":
            emoji_label.config(text="⛈️")

        elif weather == "Snow":
            emoji_label.config(text="❄️")

        else:
            emoji_label.config(text="🌤️")

    except:

        messagebox.showerror(
            "Error",
            "Network Error!"
        )

# ================= HEADING =================

heading = Label(
    root,
    text="Weather App",
    font=("Poppins", 28, "bold"),
    bg="#121212",
    fg="#00FFD1"
)

heading.pack(pady=25)

# ================= CITY INPUT =================

city_label_input = Label(
    root,
    text="Enter City Name",
    font=("Poppins", 14),
    bg="#121212",
    fg="white"
)

city_label_input.pack(pady=10)

city_entry = Entry(
    root,
    font=("Poppins", 14),
    width=24,
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    border=0,
    justify="center"
)

city_entry.pack(ipady=8)

# ================= BUTTON =================

search_btn = Button(
    root,
    text="Get Weather",
    font=("Poppins", 14, "bold"),
    bg="#00FFD1",
    fg="black",
    activebackground="#00c9a7",
    activeforeground="white",
    padx=20,
    pady=10,
    border=0,
    cursor="hand2",
    command=get_weather
)

search_btn.pack(pady=25)

# ================= WEATHER EMOJI =================

emoji_label = Label(
    root,
    text="🌍",
    font=("Arial", 50),
    bg="#121212",
    fg="white"
)

emoji_label.pack()

# ================= CITY =================

city_label = Label(
    root,
    text="",
    font=("Poppins", 22, "bold"),
    bg="#121212",
    fg="white"
)

city_label.pack(pady=10)

# ================= TEMPERATURE =================

temp_label = Label(
    root,
    text="",
    font=("Poppins", 40, "bold"),
    bg="#121212",
    fg="#00FFD1"
)

temp_label.pack()

# ================= WEATHER =================

weather_label = Label(
    root,
    text="",
    font=("Poppins", 18),
    bg="#121212",
    fg="white"
)

weather_label.pack(pady=5)

# ================= DETAILS =================

details_label = Label(
    root,
    text="",
    font=("Poppins", 14),
    bg="#121212",
    fg="gray"
)

details_label.pack(pady=15)

# ================= FOOTER =================

footer = Label(
    root,
    text="Developed by Chinmayi 💻",
    font=("Poppins", 10),
    bg="#121212",
    fg="gray"
)

footer.pack(side=BOTTOM, pady=10)

# ================= RUN =================

root.mainloop()