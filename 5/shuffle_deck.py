# Package to call HTTP request
import requests

# URL of API shuffle deck
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"

payload = {}
headers = {}

# Call API and gain response as JSON
response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
