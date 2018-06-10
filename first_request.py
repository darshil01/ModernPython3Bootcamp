import requests

url = "https://icanhazdadjoke.com/search"
parameters = {
    "limit": 1,
    "query": "dog",
}

headers = {
    "Accept": "application/json",
}

response = requests.get(url, headers=headers, params=parameters).json()

print(response)

# print(f"your request to {url} came back with status code {response['status']}")
# print(f"Joke id: {response['id']}")
# print(f"{response['joke']}")