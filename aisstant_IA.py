import pyttsx3  #pip install pyttsx3          no necesary internet
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import pyaudio #pip install pyaudio
import os
import random



engine = pyttsx3.init()
engine.setProperty('rate', 180) # Velocidad de habla
engine.setProperty('volume', 0.9) # Volumen de la voz
voices = engine.getProperty('voices') # Lista de voces disponibles
engine.setProperty('voice', voices[1].id) # Cambiar a la segunda voz disponible

text = "Hello, I am IA asistant"
def speak(text):
    engine.say(text)
    engine.runAndWait()
#speak(text)

def time():
    time = datetime.datetime.now().strftime("%I:%M: %p")
    speak(f"The time is {time}")

#time()
def date():
    day = int(datetime.datetime.now().day)
    month= int(datetime.datetime.now().month)
    year= int(datetime.datetime.now().year)    
    speak(f"The date is, day  {day}, of the  month {month}, of the year {year}")
#date()
def play_song():
    songs_dir = "C:\\Users\\User\\Music" #forlder where save your songs 
    songs = os.listdir(songs_dir)
    song_choice = random.choice(songs)
    os.startfile(os.path.join(songs_dir, song_choice))

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') # lenguague english "in"
        #query = r.recognize_google(audio, language='es-ES') # lenguague spanish

        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

#takeCommand()

""" def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close() """

if __name__ == "__main__":
    #time() fuction for start
    speak("Hello sir , say me your instructions")
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'play song' in query:
            play_song()

        elif 'offline' in query:
            speak("I am offline")
            quit()
       
