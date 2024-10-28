import google.generativeai as genai

# Config API with API-Key get from Google AI Studio
genai.configure(api_key="YOUR_API_KEY")
# Init the model to use
model = genai.GenerativeModel("gemini-1.5-flash")

# Call API and chat with Gemini
response = model.generate_content("Explain how AI works")
print(response.text)    # Print response