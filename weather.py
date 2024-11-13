import requests


def main():
    url = "https://wttr.in/{}?nTqM&lang=ru"
    url = url.format(input("Введите город: "))
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)


if __name__=="__main__":
    main()