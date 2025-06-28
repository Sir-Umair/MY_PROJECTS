import google.generativeai as genai

print("Gemini AI Client Initialized")

# Configure your Gemini API key
genai.configure(api_key="")

model = genai.GenerativeModel('gemini-1.5-flash')

command = '''[10:57 PM, 6/26/2025] Zain Zaidi: Bhai chiya ha
[10:58 PM, 6/26/2025] Zain Zaidi: Mojha 
[10:58 PM, 6/26/2025] Zain Zaidi: Agar to Ghar per ha       
[10:58 PM, 6/26/2025] Zain Zaidi: To mara Ghar patra hi dy please. If you don't 
mind
[10:58 PM, 6/26/2025] UMAعR💫: Garri key say he nikalney ha 
[10:58 PM, 6/26/2025] UMAعR💫: Mubeen say rabta krlay Haji ghr ha
[10:59 PM, 6/26/2025] Zain Zaidi: Kiu ka ma Ghar nahi ho    
[10:59 PM, 6/26/2025] UMAعR💫: So masla 
ha'''

response = model.generate_content([
    "You are a person whose name is Zain. "
    "You analyze the chat and talk like Zain. "
    "Give short and interesting responses please. You can speak Urdu as well when asked.",
    command
])

print(response.text)
