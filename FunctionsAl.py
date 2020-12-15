'''Alexa main functions'''
import pyttsx3,speech_recognition as sr,datetime,smtplib,sys,time,os 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)
engine.setProperty('volume', 1)
global gain
gain=False
def speak(audio):
        engine.say(audio)
        engine.runAndWait()

def PrSpeak(audio):
        for char in audio:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
        print()
        engine.say(audio)
        engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            PrSpeak("Good Morning!")

        elif hour>=12 and hour<18:
            PrSpeak("Good Afternoon!")   

        else:
            PrSpeak("Good Evening!")  

        PrSpeak("I Am Alexa My Friend Please Tell Me How May I Help You")  

def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            PrSpeak("Listening...")
            audio = r.listen(source)

        try:
            PrSpeak("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n")

        except Exception:
            # print(e)    
            PrSpeak("Say that again please...")  
            return "None"
        return query

def sendEmail(to, content):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("suvanshchoudhary60@gmail.com","1rFYz92008151827suvanshchoudhary60@gmail.com")
            server.sendmail("suvanshchoudhary60@gmail.com",to,content)
            server.close()

def Quit():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<18:
            PrSpeak("Bye Have A Nice Day Say Alexa To Call Me Again")

        else :
            PrSpeak("Bye Good Night Say Alexa To Call Me Again I Am Always There With You")

def closeFile(exeName,NameOfFile):
            os.system(f"TASKKILL /F /IM {exeName}")
            PrSpeak(f"Closed {NameOfFile}")

def start():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            typeing("listening...\n")
            audio = r.listen(source)

        try:
            typeing("Checking Alexa In Your Command\n")
            query = r.recognize_google(audio, language='en-in')
            if "alexa" in query:
                typeing("Starting This App\n")
        except Exception:
            typeing("Alexa Was Not There In Your Command Say Alexa To Start This App\n")
            return "None"
        return query

def typeing(text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.00000000000000000000000000000000000001)

