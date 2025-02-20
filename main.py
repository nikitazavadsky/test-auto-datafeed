import requests

URL = "https://cdn.searchspring.net/help/feeds/searchspring.xml"

response = requests.get(URL)

if response.ok:
    with open("output/datafeed.xml", "w") as file:
        file.write(response.text)
