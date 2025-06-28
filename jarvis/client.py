import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key="")

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(
    "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please. Now answer this: Hello Jarvis, can you open Google, YouTube, or GitHub? Also, play some music from my library or fetch the latest news for me."
)

print(response.text)
