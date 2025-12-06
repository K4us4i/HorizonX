# Local Community Help
# Community Connectivity
from flask import Flask, render_template, request
import requests # type: ignore

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        event = request.form.get("event")
        url = "https://calendar.bloggernepal.com/api/today"

        headers = {"Content-Type": "application/json"}
        payload = {"text": event_text} # type: ignore

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        result = data["result"]["type"]

    return render_template("page.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

