# Local Community Help
# Community Connectivity
from flask import Flask, render_template, request
import requests # type: ignore

app = Flask(__name__)

@app.route("/events")
def get_events():
    url = "https://calendar.bloggernepal.com/api/today"
    
    headers = {
        "Authorization": "Bearer YOUR_EVENTBRITE_TOKEN"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # return jsonify(data)

@app.route("/alerts")
def get_alerts():
    url = "https://api.weather.gov/alerts/active"
    response = requests.get(url)
    data = response.json()

    # return jsonify(data)

@app.route("/")
def home():
    return render_template("page.html")


if __name__ == "__main__":
    app.run(debug=True)


