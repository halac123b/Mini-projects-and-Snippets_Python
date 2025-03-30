import json

with open("data.json", "r") as file:
    # Read string dạng json as a dict
    data = json.load(file)

# Convert ngược lại dict thành json string
jsonStr = json.dumps(data)