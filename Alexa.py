from genericpath import exists
import os,wikipedia,webbrowser,subprocess,pywhatkit as kit
import random
import FunctionsAl as FA
def startAlexa():
    dir ="C:\\songsAlexa"
    if not os.path.exists(dir):
        os.makedirs(dir,exist_ok=True)
    '''
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Author:::::::: Suvansh
    Contact::::::: suvanshchoudhary60@gmail.com
    Date:::::::::: 10-12-2020
    python:::::::: 3.6.8
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    '''
    global a
    firsttime=True
    FA.PrSpeak("Say Alexa To Start This App")
    while True:
        query = FA.start().lower()
        while "alexa" not in query:
            if "alexa" in query:
                break
            else:
                query=FA.start().lower()
        FA.typeing("Starting This App...\n")
        if firsttime==True:
            FA.wishMe()
        while True:
            query = FA.takeCommand().lower()
        # !-------------------------------------------------------------------------------------------------    
    #? ------------------------------------------Searches--------------------------------------------------------
        # !-------------------------------------------------------------------------------------------------    

            if 'full wikipedia' in query:
                try:
                    FA.PrSpeak('Searching Wikipedia...')
                    query = query.replace("full wikipedia", "")
                    results = wikipedia.summary(query, sentences=999999999999)
                    FA.PrSpeak("According To Wikipedia...")
                    print(results)
                    FA.speak(results)
                except:
                    FA.PrSpeak(f"Sorry I Was Not Able To Desplay The Result Because Of Some Issues")

            elif 'ful wikipedia' in query:
                try:
                    FA.PrSpeak('Searching Wikipedia...')
                    query = query.replace("ful wikipedia", "")
                    results = wikipedia.summary(query, sentences=999999999999)
                    FA.PrSpeak("According To Wikipedia...")
                    print(results)
                    FA.speak(results)
                except:
                    FA.PrSpeak(f"Sorry I Was Not Able To Desplay The Result Because Of Some Issues")

            elif 'wikipedia' in query:
                try:
                    FA.PrSpeak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    FA.PrSpeak(results)
                except:
                    FA.PrSpeak(f"Sorry I Was Not Able To Desplay The Result Because Of Some Issues")
# todo---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #!------------------------------------------------------------------------------------------------------
    #?--------------------------------------------Opens-----------------------------------------------------------------------
        #!------------------------------------------------------------------------------------------------------
            elif 'open gmail' in query:
                FA.PrSpeak("Opening Gmail...")
                webbrowser.open("gmail.com")
                FA.PrSpeak("Opened Gmail")

            elif 'open gaana' in query:
                FA.PrSpeak("Opening Ganna")
                webbrowser.open("gaana.com")
                FA.PrSpeak("Opened Gaana")

            elif 'open stack overflow' in query:
                FA.PrSpeak("Opening StackOverFlow...")
                webbrowser.open("stackoverflow.com")
                FA.PrSpeak("Opened StackOverFlow")

            elif 'open google' in query:
                FA.PrSpeak("Opening Google...")
                webbrowser.open("google.com")
                FA.PrSpeak("Opened Google")

            elif 'open youtube' in query:
                FA.PrSpeak("Opening YouTube...")
                webbrowser.open("youtube.com")
                FA.PrSpeak("Opened YouTube")

            elif 'open ms teams' in query or 'open microsoft teams' in query:
                FA.PrSpeak("Opening MicroSoftTeams...")
                webbrowser.open("teams.microsoft.com")
                FA.PrSpeak("Opened MicrosoftTeams")

            elif 'open code' in query or "open vs code" in query or 'open visual studio code'in query:
                try:
                        FA.PrSpeak("Opening Visual Studio Code...")
                        codePath = "C:\\Users\\suvan\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(codePath)
                        FA.PrSpeak("Opened Visual Studio Code")
                except:
                    FA.PrSpeak(f"Sorry My Friend I Was Not Able To Open Visual Studio Code Because Of Some Issue")


            elif 'open file explorer'in query or 'open explorer' in query:
                FA.PrSpeak("Opening File Explorer...")
                subprocess.Popen('explorer')
                FA.PrSpeak("Opened File Explorer")

            elif 'open zoom' in query:
                try:
                    FA.PrSpeak("Opening Zoom...")
                    zoom = FA.path.get("zoom")
                    os.startfile(zoom)
                    FA.PrSpeak("Opened Zoom")
                except:
                    FA.PrSpeak(f"Sorry My Friend I Was Not Able To Open Zoom Because Of Some Issue")

            # !-------------------------------------------------------------------------------------------------------------------------
    # ?--------------------------------------------Closes------------------------------------------------------------------------
            # !--------------------------------------------------------------------------------------------------------------------------
            elif 'close file explorer' in query:
                try:
                    FA.PrSpeak("Closing File Explorer...")
                    FA.closeFile("explorer.exe","Explorer")
                    FA.PrSpeak("Closed File Explorer")
                except:
                        FA.PrSpeak(f"Sorry My Friend I Was Not Able To Close File Explorer")

            elif 'close hitman' in query:
                try:
                    FA.PrSpeak("Closing Hitman...")
                    os.system("TASKKILL /F /IM HMA.exe")
                    FA.PrSpeak("Closed Hitman")
                except:
                    FA.PrSpeak(f"Sorry My Friend I Was Not Able To Close Hitman")

            elif 'close code' in query or 'close vs code' in query or 'close visual studio code' in query:
                try:
                    FA.PrSpeak("Closing Visual Studio Code...")
                    os.system('TASKKILL /F /IM Code.exe')
                    FA.PrSpeak("Closed Visual Studio Code")
                except:
                    FA.PrSpeak(f"Sorry My Friend I Was Not Able To Close Visual Studio Code")
                    
            elif 'close zoom' in query:
                try:
                    FA.PrSpeak("Closing Zoom...")
                    os.system('TASKKILL /F /IM Code.exe')
                    FA.PrSpeak("Closed Zoom")
                except:
                    FA.PrSpeak(f"Sorry My Friend I Was Not Able To Close Zoom")
            # !--------------------------------------------------------------------------------------------------------------------------
    #? ---------------------------------------------Others--------------------------------------------------------------------------
            # !--------------------------------------------------------------------------------------------------------------------------
            elif 'codewithharry'in query:
                FA.PrSpeak("Opening Channel CodeWithHarry...")
                webbrowser.open("www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww")
                FA.PrSpeak("Opened Channel CodeWithHarry")
            
            elif 'search in youtube' in query:
                FA.PrSpeak("Searching Youtube...")
                a=query
                a=a.split("youtube")
                kit.playonyt(a[1])
                FA.PrSpeak("Searched Youtube")

            elif 'shut down my pc' in query:
                try:
                    FA.PrSpeak("Shutting Down Your Pc And Wating For 10 Seconds For Your Cancel Shut Down Command...")
                    kit.shutdown(10)
                except:
                    FA.PrSpeak(f"Unable To Shut Down Your Pc")
            
            elif 'cancel shut down' in query:
                try:
                    FA.PrSpeak("Cancelling...")
                    kit.cancelShutdown()
                    FA.PrSpeak("Canceled")
                except:
                    FA.PrSpeak("Unable To Cancel Shutdown")

            elif 'play music' in query:
                try:
                    music_dir = "C:\\songsAlexa"
                    songs = os.listdir(music_dir)
                    if len(songs)>1:
                        FA.PrSpeak("Playing Random Music...")
                        os.startfile(os.path.join(music_dir, songs[random.randint(1,len(songs))]))
                        FA.PrSpeak("Played Random Music")
                    else:
                        FA.PrSpeak("Playing Random Music...")
                        os.startfile(os.path.join(music_dir, songs[0]))
                        FA.PrSpeak("Played Random Music")
                    FA.PrSpeak("If You Want To Add Songs You Can Go To c:\\songsAlexa And Add More Songs In It")
                except:
                    FA.PrSpeak(f"Sorry I Was Not Able To Play Music Please Add Songs In C:\\songsAlexa")

            elif 'send email' in query:
                try:
                    FA.speak("Enter The Email Of The Person Whom You Want To send Email")
                    send=input("Enter The Email Of The Person Whom You Want To Send Email: ")
                    FA.speak("Enter Your Content")
                    con=input("Enter Your Content: ")
                    FA.PrSpeak("Sending Email...")
                    FA.sendEmail(send,con)
                    FA.PrSpeak("Email Sent")
                except Exception as e:
                    FA.PrSpeak(f"Sorry My Friend I Am Not Able To Send This Email") 

            elif 'the time' in query:
                FA.PrSpeak("Telling The Time...")
                strTime = FA.datetime.datetime.now().strftime("%H:%M:%S")    
                FA.PrSpeak(f"The Time Is {strTime}")

            #! ----------------------------------------------------------------------------------------------------------------------------------------------------------
    #?----------------------------------------------Talks--------------------------------------------------------------------------------------------
            # !-----------------------------------------------------------------------------------------------------------------------------------------------------------

            elif 'your name' in query:
                FA.PrSpeak('My Name Is Alexa')

            elif 'your version' in query:
                FA.PrSpeak('I Am 1.0.4 Verson Of Alexa')

            elif 'your pet name' in query:
                FA.PrSpeak('I Don\'t Have Any Pet')

            elif 'your favourite pet' in query:
                FA.PrSpeak('My Favourite Pet Is Cat')

            elif 'oh yes' in query:
                FA.PrSpeak('I Think That You Are So Happy')

            # !---------------------------------------------------------------------------------------------------------------------------------------------------------------
    #?---------------------------------------------ImportWarning----------------------------------------------------------------
            # !---------------------------------------------------------------------------------------------------------------------------------------------------------------
            elif 'alexa sleep'in query:
                FA.Quit()
                firsttime=False
                break
            
            elif 'alexa close yourself' in query:
                FA.PrSpeak("Closing...")
                FA.PrSpeak("Closed")
                a.close()
                exit()
            
            else:
                pass
startAlexa()