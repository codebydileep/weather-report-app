from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "365773c1f9dada35006a8e8a3456f048"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city_name = request.form.get("city")
        if city_name:
            # Fetch weather data from OpenWeatherMap API
            request_url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
            response = requests.get(request_url)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": city_name,
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"].capitalize(),
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"],
                }
            else:
                weather_data = {"error": "Failed to fetch weather data. Please check the city name."}
    return render_template("index.html", weather_data=weather_data)


if __name__ == "__main__":
    app.run(debug=True)
