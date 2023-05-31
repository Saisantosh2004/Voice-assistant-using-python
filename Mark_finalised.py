import pyttsx3  # pip install pyttsx3(library)..converts text to speech
import speech_recognition as sr  # pip install speechRecognition..for speech recognition
import datetime  # contains all the data related to calender
import wikipedia  # pip install wikipedia
import webbrowser  # opens any website mentioned as a string
import os  # provides functions so user can interact with the system's operating system
import smtplib  # module which is used for sending mails remotely with google
from googlesearch import *
from PyDictionary import PyDictionary
from iso_language_codes import *
import pywhatkit
import pyautogui
import psutil
import time
from playsound import playsound
from GoogleNews import GoogleNews
import ssl
from email.message import EmailMessage

engine = pyttsx3.init('sapi5')  # sapi5 is a microsoft API used for speech recognition and synthesis in windows
voices = engine.getProperty('voices')  # gets the voices from the API
# print(voices[1].id) #voices[1].id is a female voice..voices[0].is a male voice
engine.setProperty('voice', voices[0].id)  # sets the voice required

def speak(audio):
    engine.say(audio)  # speaks whatever is asked
    engine.runAndWait()  # after speaking waits for a command

def wishMe():  # used for salutations
    hour = int(datetime.datetime.now().hour)  # datetime module used for getting the current hour
    if hour >= 5 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour >= 0 and hour < 5:
        print("An early morning for you, i see ")
        speak("An early morning for u. i see")

    elif hour >= 12 and hour < 17:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    # first speak func is implemented then greeting based on datetime is implemented
    else:
        print("Good evening")
        speak("Good Evening!")

    print("Hi there ,I am Mark. how may I help you today ?")  # salutations
    print("please speak now ")
    speak("Hi there , I am Mark. how may I help you today ?")
    speak("please speak now ")


def screen_shot():  # for clicking screenshots
    ss = pyautogui.screenshot()
    try:
        ss.save("ss_1.png")
    except Exception as e:
        print(e)
    speak("Screenshot is taken sir")


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def takeCommand():
    # It takes microphone input from the user and returns string output
    # energy threshold takes minimum sound level for assistant to run
    # can be used in noisy places to detect commands only above certain level
    r = sr.Recognizer()  # recogniser helps in detecting the audio input
    with sr.Microphone() as source:  # microphone source is sr.mic

        print("Listening...")
        # speak("Listening...")
        r.pause_threshold = 0.8  # it is the time in sec where nothing is spoken and
        # after that time next phase of code is implemented
        audio = r.listen(source)

    try:  # used when error can be contacted
        print("Configuring...")
        # speak("Configuring...")
        query = r.recognize_google(audio, language='en-in')
        # performs speech recognition using google API
        # google API used here is same as the one in android phones
        print(f"You have said: {query}\n")  # fstring used here
        speak(f"You have said: {query}\n")

    except Exception as e:
        # if google API doesnt recognise in try..exception is run
        # print(e)
        print("sorry, could not hear you. please repeat ")
        #speak("sorry, could not hear you. please repeat ")
        return "None"  # none is a string here
    return query


def alarm():
    # Infinite Loop
    while True:
        # Set Alarm
        set_alarm = (f"{20}:{17}:{20}")

        # Wait for one seconds
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm:
            print("Time to Wake up")
            # Playing sound
            # for playing note.mp3 file
            playsound("C:\\Users\\pc\\OneDrive\\Desktop\\alarm1.mp3")
if __name__ == "__main__":
    wishMe()  # if wishMe is inside loop..assistant will keep wishing until stack overflow
    while True:  # infinite while loop
    #if 1:
        query = takeCommand().lower()  # converts command into lowercase strings
        # lowercase is used so that query can match the web browser module commands
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")  # replaces all occurences of wikipedia with "" in output
            results = wikipedia.summary(query, sentences=2)  # returns summary of 2 sentences from wikipedia
            print("According to Wikipedia")
            speak("According to Wikipedia")
            # print("According to Wikipedia")
            print(results)  # prints the output from wikipedia
            speak(results)  # speaks the output from wikipedia

        elif 'how are you' in query:
            print("I am fine, how about you ? ..what can i do for u then ")
            speak("I am fine, how about you ? ..what can i do for u then ")

        elif 'tell me a joke' in query:
            print("Why do we tell actors to break a leg? Because every play has a cast")
            speak("Why do we tell actors to break a leg? Because every play has a cast")

        elif 'i did not find it funny' in query:
            print("sorry is there something else i can help you with.. ")
            speak("sorry is there something else i can help you with.. ")

        elif 'stop' in query:
            print("Alright.. I shall stop. To access me run the code again ")
            speak("alright.. i shall stop. To access me run the code again ")
            exit(0)

        elif 'open youtube' in query:
            print("opening youtube")
            speak('opening youtube')
            webbrowser.open("youtube.com")

        elif 'open spotify' in query:
            print("opening spotify")
            speak('opening spotify')
            webbrowser.open("spotify.com")  # webbrowser module opens the site i.e., the string in parameter

        elif 'open google' in query:
            # speak("What do you want me to search")
            query = query.replace("open google", "")

            for url in search(query):
                # print(url)
                webbrowser.open(url)
                break
            # print("opening google")
            # speak('opening google')
            # webbrowser.open("google.com")

        elif 'charge' in query:
            # returns a tuple
            print(query)
            battery = psutil.sensors_battery()

            print("Battery percentage : ", battery.percent)
            print("Power plugged in : ", battery.power_plugged)

            # converting seconds to hh:mm:ss
            print("Battery left : ", convertTime(battery.secsleft))

        elif 'open stack overflow' in query:
            print("opening stack overflow")
            speak('opening stack overflow')
            webbrowser.open("stackoverflow.com")

        elif 'open notepad' in query:
            print("opening notepad...")
            os.system("C:\\Windows\\notepad.exe")

        elif 'play music' in query:
            music = 'C:\\UK260\\music'  # path of music files
            songs = os.listdir(music)  # lists all song files
            print(songs)
            print("playing a song")
            speak("playing a song")
            os.startfile(os.path.join(music, songs[0]))  # starts the file where the data is stored

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time currently is {strTime}")  # fstring is used here
            speak(f"the time currently is {strTime}")

        elif 'play on youtube' in query:
            query = query.replace('play on youtube', "")
            speak('playing ' + query)
            pywhatkit.playonyt(query)

        elif 'meaning of' in query:
            query=query.replace("meaning of","")
            dict = PyDictionary()
            meaning = dict.meaning(query)
            print(f"The meaning of {query} is:{meaning}")
            speak(f"The meaning of {query} is:{meaning}")

        elif "translate" in query:
            query=query.replace("translate","")
            speak("To which language you want to  convert sir!")
            query2=takeCommand()
            print(f"You want to convert it to {query2}")
            dict = PyDictionary()
            languages = language_dictionary()
            l1=list(languages.keys())
            l2=list(i['Name'] for i in languages.values())
            lang=l1[l2.index(query2)]
            translation = dict.translate(query,lang)
            print(translation)
            speak(translation)

        elif 'send whatsapp message' in query:
            query = query.replace('send whatsapp message', "")
            speak('sending message ' + query)
            pywhatkit.sendwhatmsg("+917993686590", "Hi, How are you?",11,16,10,True,12)

        elif 'take screenshot' in query:
            screen_shot()
            # query=query.replace('take screenshot',"")

        elif 'convert to handwriting' in query:
            query = query.replace('convert to handwriting', "")
            speak('converting... ' + query)
            pywhatkit.text_to_handwriting("Hello Uday", "filename.png")

        elif 'google news' in query:
            googlenews = GoogleNews('en')
            googlenews.search('India')
            googlenews.getpage(2)
            googlenews.result()
            n = googlenews.gettext()
            for i in n:
                print(i)
                speak(i)
        elif 'set alarm' in query:
            alarm()
        elif 'open coding platform' in query:
            codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.10\IDLE (Python 3.10 64-bit).lnk"  # path of program required
            print("opening your coding platform now")
            speak("opening your coding platform now")
            os.startfile(codePath)  # opens the program

        elif 'open private files' in query:
            vpath = ''
            vid = os.listdir(vpath)
            print(vid)  # currently songs being played..video also being played as song
            print("opening private files")  # needs changes to play video
            speak("opening private files")
            os.startfile(os.path.join(vpath, vid[0]))

            # requires third party permissions from google account..not able to access the permission feature yet
        # so unable to send mails right now
        elif 'send email' in query:
            # Define email sender and receiver
            email_sender = 'freakyuser26@gmail.com'
            email_password = 'skewzwsjefnhwuqp'
            email_receiver = 'ukreddymanda@gmail.com'

            # Set the subject and body of the email
            subject = 'check out our new code!'
            body = """This is our EE project"""
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)
            # Add SSL (layer of security)
            context = ssl.create_default_context()
            # Log in and send the email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            print("Email successfully sent!")

print("you have exited from loop")



