import requests


def main():
    places = ["London", "Cherepovets", "Sheremetyevo"]
    payload = {"n": "",
               "T": "",
               "q": "",
               "M": "",
               "lang": "ru"
            }
    for place in places:
        url = "https://wttr.in/{}"
        url = url.format(place)
        response = requests.get(url, params = payload)
        response.raise_for_status()
        print(response.text)


if __name__=="__main__":
    main()