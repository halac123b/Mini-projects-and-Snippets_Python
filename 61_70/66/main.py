import google.generativeai as genai

GOOGLE_API_KEY='GOOGLE_API_KEY'

# Authenticate with API key
genai.configure(api_key=GOOGLE_API_KEY)

# Chọn model rồi đặt câu hỏi, cũng khá giống với OpenAI
model = genai.GenerativeModel('models/gemini-2.0-flash')
response = model.generate_content("Please give me python code to sort a list.")
print(response.text)