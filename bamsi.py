import datetime
import os
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import pyyoutube




# to take voices use sapi5
engine =   pyttsx3.init("sapi5") 
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>= 12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("I am Bamsi how can i help you")

def takeCommand():
    # This function take command from user through microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        # Logic for executing task on queries
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak(f"According to wikipedia")
            speak(results)

        elif "play video" in query:
            speak("Playing your Video")
            videos_dir = "C:\\Users\\rasoo\\Videos\\openshot videos\\all videos"
            videos = os.listdir(videos_dir)
            print(videos)
            os.startfile(os.path.join(videos_dir, videos[3]))

        elif "open youtube" in query:
            speak("Opening Youtube")
            chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('google-chrome',webbrowser.BackgroundBrowser(chrome_path),1)
            webbrowser.get('google-chrome')
            webbrowser.open("https://youtube.com")       


        elif "the time" in query:
            time_ = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time_}")



        elif 'quit' in query:
            exit()

        
