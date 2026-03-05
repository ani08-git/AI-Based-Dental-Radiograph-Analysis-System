import requests
import os

url = "http://127.0.0.1:5000/analyze"

for file in os.listdir():

    if file.endswith(".png") or file.endswith(".jpg"):

        files = {"image": open(file, "rb")}

        response = requests.post(url, files=files)

        print("Image:", file)
        print(response.json())
        print()