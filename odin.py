import pyttsx3                          #pip install pyttsx3, 'sapi5' api Engine
import datetime                         #Builtin Module    
import speech_recognition as sr         #pip install pip install SpeechRecognition, speech Recognition through Microphone      
import wikipedia                        #pip install wikipedia, for querying wikipedia
import webbrowser                       #pip install webbrowser, for doing browser operations
import os                               #Builtin module
import smtplib                          #pip install smtplib, for sending Emails
import requests, json



engine = pyttsx3.init('sapi5')                  
voices = engine.getProperty('voices')
# print(voice)
engine.setProperty('voices', voices[0].id)      #voices[0] is for a Male Voice, voices[1] is for a Female voice
# print(voices[1].id)


'''Function allows Odin to speak through pyttsx3 modules sapi5 api'''
def speak(audio):           
    engine.say(audio)
    engine.runAndWait()

'''Function will make Odin greet you depending on the time of the day whenever the program is run'''
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    
    else:
        speak("Good Evening Sir")
    speak("I am Odin, your personal Assistant, How may I help you")

'''Function makes use of SpeechRecognition module to understand users Query'''
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing") 
        query = r.recognize_google(audio, language='en-in')
        print(f"You just said...: {query}\n")

    except Exception as e:      #Just in case the function fails to unserstand the Query, the Exception will execute asking user to repeat it.
        # print(e)

        print("Can you please say that again") 
        return "None"
    return query

'''Function uses smtplib module to send an Email'''
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to,content)
    server.close()

      
if __name__ == "__main__":
    # speak("testing")
    WishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'new wallpapers' in query:
            webbrowser.open("unsplash.com")     

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Indra\\Downloads\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, The time is {strTime}")   

        elif 'open visual studio' in query:
            codePath = "C:\\Users\\Indra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open vmware' in query:
            codePath = "C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe"
            os.startfile(codePath)

        elif 'open c drive' in query:
            codePath = "C:\\"
            os.startfile(codePath)

        elif 'open my folder' in query:
            codePath = "C:\\Indra"
            os.startfile(codePath)
               
        elif 'open local wallpapers' in query:
            codePath = "C:\\Indra\\walls"
            os.startfile(codePath)

        # elif 'Run Minecraft' in query:
        #     codePath = "C:\\Indra\\Minetest\\minetest-5.2.0-win64\\bin\\minetest.exe"
        #     os.startfile(codePath)    

        elif 'open download' in query:
            codePath = "C:\\Users\\Indra\\Downloads"
            os.startfile(codePath)


        elif 'send email' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "youremail@gmail.com"
                sendEmail(to, content)
                speak("Email sent")
                
            except Exception as e:
                # print(e)
                speak("Sorry sir, Unable to send the Email")

        elif 'goodbye' in query:
            speak("goodbye sir, and have a great day ahead!")
            exit()

        elif 'introduce yourself' in query:
            speak("Hello there, I am Odin, I am your personal Assistant, I was created as a Hobby project by Indrajeet Sohoni, Currently I can assist you with Opening google, Opening youtube, playing some music, sending email, Opening Applications")    

        elif 'who are you' in query:
            speak("Hello there, I am Odin, I am your personal Assistant")

        elif 'who made you' in query:
            speak("Ohh, I was made by Indrajeet Sohoni") 

        # elif ''       


