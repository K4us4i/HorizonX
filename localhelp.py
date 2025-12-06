# Local Community Help
# Community Connectivity
from flask import Flask, render_template, request, jsonify
# import requests

app = Flask(__name__)

@app.route("/events")
def get_events():
     url = "https://date.nager.at/api/v3/PublicHolidays/2025/AT"
    
     headers = {"Authorization": "Bearer YOUR_EVENTBRITE_TOKEN"
    }

    # response = requests.get(url, headers=headers)
    # data = response.json()
    # return jsonify(data)

@app.route("/alerts")
def get_alerts():
    url = "https://newsdata.io/api/1/latest?apikey=pub_0862588a38234c4caf78bfb3b8f03d44&q=news"
   # response = requests.get(url)
    #data = response.json()
   # return jsonify(data)

@app.route("/")
def home():
    return render_template("pages.html")


if __name__ == "__main__":
    app.run(debug=True)


