import requests

while True:

    city = input("Enter City Name :- ")

    url = url = f"https://wttr.in/{city}?format=3"

    response = requests.get(url)

    wether = response.text

    print(f"{city} Temprature is :- ", wether)
