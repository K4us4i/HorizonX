# Local Community Help
# Community Connectivity
import requests
response = requests.get("https://calendar.bloggernepal.com/api/today")
data=response.json()

response=requests.post("https://calendar.bloggernepal.com/api/today", json)
