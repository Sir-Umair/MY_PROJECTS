import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary
import requests
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="")

# Speak function
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Gemini integration
def aiProcess(command):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(command)
        return response.text
        print("AI Response:", response.text)
    except Exception as e:
        return f"Error: {e}"

# Command handler
def processcommands(command):
    if "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")
    elif "open github" in command:
        webbrowser.open("https://github.com/")
    elif command.lower().startswith("play"):
        song = command.split(" ")[1]
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in your music library.")
    elif "news" in command:
        key = "f83d1c832887497286555e0db37ff1a2"
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={key}"
        try:
            response = requests.get(url)
            news_data = response.json()
            articles = news_data.get("articles")
            if articles:
                speak("Here are the top news headlines.")
                for i, article in enumerate(articles[:5], start=1):
                    speak(f"Headline {i}: {article['title']}")
            else:
                speak("Sorry, I couldn't find any news.")
        except Exception as e:
            speak("There was an error fetching the news.")
            print("Error:", e)
    else:
        response = aiProcess(command)
        speak(response)
        print("i can  open google, youtube, github and play music from my library")

# Main function
if __name__ == "__main__":
    speak("Initializing Jarvis....")

    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening......")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

        print("RECOGNIZING....")
        word = r.recognize_google(audio)
        print("You said:", word)

        if word.lower() == "jarvis":
            speak("Yes sir, how can I help you?")

            with sr.Microphone() as source:
                print("ACTIVATED SUCCESFULLY......")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                print("COMMAND IS :", command)
                processcommands(command.lower())

    except sr.WaitTimeoutError:
        print("Mic timeout: no speech detected.")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except Exception as e:
        print("Error: {0}".format(e))
