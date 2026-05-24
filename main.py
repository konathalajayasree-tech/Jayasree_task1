import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os



engine = pyttsx3.init()

def speak(text):

    print(text)

    engine.say(text)

    engine.runAndWait()




def listen():

    fs = 44100
    seconds = 5

    print("Listening...")

    # RECORD AUDIO
    recording = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=1,
        dtype='int16',

        # YOUR MICROPHONE DEVICE
        device=1
    )

    sd.wait()

    # SAVE AUDIO
    write("output.wav", fs, recording)

    recognizer = sr.Recognizer()

    try:

        with sr.AudioFile("output.wav") as source:

            audio = recognizer.record(source)

            text = recognizer.recognize_google(audio)

            print("You said:", text)

            return text.lower()

    except sr.UnknownValueError:

        print("Could not understand audio")

        return ""

    except sr.RequestError:

        print("Internet connection issue")

        return ""

    except Exception as e:

        print("Error:", e)

        return ""




speak("Hello Jayasree, your voice assistant is ready")


while True:

    command = listen()

  

    if "hello" in command:

        speak("Hello Jayasree")


   

    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak("Current time is " + current_time)




    elif "date" in command:

        today = datetime.datetime.now().strftime("%d %B %Y")

        speak("Today's date is " + today)


  

    elif "who is" in command:

        person = command.replace("who is", "")

        try:

            info = wikipedia.summary(person, sentences=2)

            print(info)

            speak(info)

        except:

            speak("I could not find information")


  

    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")


   

    elif "open google" in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")


   

    elif "play music" in command:

        speak("Opening music folder")

        os.startfile("C:\\Users\\heman\\Music")


   

    elif "stop" in command or "exit" in command:

        speak("Goodbye Jayasree")

        break


   
    elif command == "":

        speak("Please speak again")


   

    else:

        speak("I heard " + command)