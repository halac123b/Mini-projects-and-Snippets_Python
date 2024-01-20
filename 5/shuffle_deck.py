# Package to call HTTP request
import requests

# URL of API shuffle deck
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"

payload = {}
headers = {}

# Call API and gain response as JSON
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Cách 2: không ghi trực tiếp parameter vào URL mà ghi vào querystring
url = "https://deckofcardsapi.com/api/deck/new/shuffle/"

querystring = {"deck_count": "6"}

headers = {
    "Cache-Control": "no-cache",
    "Postman-Token": "dd1d8ca5-7000-21b2-2230-39969d585419",
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
# Parse JSON ra dict
deck = response.json()
# Access vào key deck_id
deck_id = deck["deck_id"]
print(deck_id)
