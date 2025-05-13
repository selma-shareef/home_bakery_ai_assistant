import google.generativeai as genai

API_KEY="AIzaSyDMsGJi-0nRlCORIuUj-lHemmu_uPdGGWE"

genai.configure(api_key=API_KEY)
model=genai.GenerativeModel("gemini-2.0-flash")

chat=model.start_chat()
resp=chat.send_message("What is the capital of India?")
print(resp)