#Here is the code for my project. You will have to download some of these libraries externally with PIP.
import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition 
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os

print("Starting garry")

engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# pronounce any given string
def speak(text):
    engine.say(text)
    engine.runAndWait()

# garry greeting user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good morning ")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon ")
        print("Good Afternoon")
    else:
        speak("good evening ")
        print("Good Evening")
    speak("I am garry.")

# garry listening to user
def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try : 
        print("Recognizing...")
        query = r.recognize_google(audio,language='en')
        print(query)
    
    except:
        print("Say that again please...")
        commands()
 
    return query


#MAIN PROGRAM
def main():
    while True:
        speak("what should I do for you?")
        print("what should I do for you?")
        query = commands()

        #logic for task execution(by query)
        if 'wikipedia' in query.lower():
            print('Searching Wikipedia')
            speak('Searching wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences =2)
            print("According to Wikepdia: " + results)
            speak(results)
        
        elif 'youtube' in query.lower():
            url = "youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            print('Opening Youtube')
            webbrowser.get(chrome_path).open(url)

        elif 'spotify' in query.lower():
            url2 = "https://open.spotify.com/"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            print('Opening Spotify')
            webbrowser.get(chrome_path).open(url2)

        elif 'the time' in query.lower():
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print('The time is: '+time)
            speak(f"the time is {time}")
            #break

        elif 'google' in query.lower():
            url = "google.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            print('Opening Google Chrome')
            webbrowser.get(chrome_path).open(url)
            
        elif 'favorite' in query.lower():
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ') 
        
        if query.lower() == 'goodbye':
            print("see you soon")
            speak("see you soon ")
            break

speak("Starting garry...")
wishMe()
main()
