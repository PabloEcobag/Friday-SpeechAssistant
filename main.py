import pywhatkit
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyjokes




listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
engine.setProperty('volume', 200)
engine.say('Hi, Im Friday')
engine.say('How can I assist you..Sir?')

engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()
def say(text):
    engine.say('Im Friday')
    engine.runAndWait()
def ask(text):
    engine.say('How can I assist you?')

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday', '')
                print(command)
            if 'repeat me' in command:
                talk(command)

    except:
        pass
    return command


def run_friday():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'who are you?' or 'who am i speaking to?' or 'whos this?' in command:
        say('Im Friday')
        talk('How can I help you today?')
        take_command()
    else:
        talk('How can I help you today?')


run_friday()