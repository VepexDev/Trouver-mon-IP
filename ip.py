from urllib import response
import requests

response = requests.get("https://api.ipify.org/?format=json")
ip = response.json()["ip"]

print(f"Ton ip est: {ip}")