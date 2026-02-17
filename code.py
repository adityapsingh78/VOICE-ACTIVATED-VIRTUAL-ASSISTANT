from httpx import request
from openai import OpenAI
from setuptools import Command
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

recognition = sr.Recognizer()
engine = pyttsx3.init()
newsapi_key = "d093053d72bc40248998159804e0e67d"
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def ai_proccess(command):
   client=OpenAI(api_key="Fill in your OpenAI API key here")

   response = client.chat.completions.create(
     model="gpt-3.5-turbo",
         messages=[
       {"role": "user", "content": command}
     ]
   )
   return response.choices[0].message.content 


def process_Command(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "play music" in c.lower():
        speak("Playing music from your library")
        musiclibrary.play_music()
    elif "news" in c.lower():
        speak("Fetching news...")
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi_key}"
        response = request.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data["articles"]
            for article in articles[:5]:
                speak(article["title"])
        else:
            speak("Failed to fetch news")
    else:
        response = ai_proccess(c)
        speak(response)
        

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I assist you today?")
    
    while True:
        # Listen for user input
        # with sr.Microphone() as source:
    
        r=recognition
        
            
        print("Recognizing...")
        
        try:
            with sr.Microphone() as source:
              print("listening...")
              audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("Yes, how can I help you?")
                with sr.Microphone() as source:
                  print("jarvis Activated, listening...")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)
                  
                  process_Command(command)
        except Exception as e:
            print("Error:{0}".format(e))