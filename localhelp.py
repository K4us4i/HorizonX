# Local Community Help
# Community Connectivity
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/events")
def get_events():
    url = "https://calendar.bloggernepal.com/api/today"
    
    headers = {
        "Authorization": "Bearer YOUR_EVENTBRITE_TOKEN"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    return jsonify(data)


