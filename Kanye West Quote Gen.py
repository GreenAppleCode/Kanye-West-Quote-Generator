import requests

def quote():
    url = requests.get("https://api.kanye.rest/")
    json_url = url.json()
    print(json_url["quote"])
    yorn = input("Do you want to hear another amazing quote?(y/n): ")
    if yorn == "y":
        quote()
    elif yorn == "Y":
        quote()
    elif yorn == "n":
        print("Alright, have a nice day!")
        exit()
    elif yorn == "N":
        print("Alright, have a nice day!")
        exit()
    else:
        print("Invalid Syntax, Closing Program...")
        exit()
quote()