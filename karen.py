from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
import webbrowser
import speekmodule
import pyttsx3, datetime, sys, wikipedia, wolframalpha, os, smtplib, random, webbrowser, pygame, subprocess

client = wolframalpha.Client('LHE7YK-3K6TV7KG68')

folder = 'C:\\DOWNLOd\\'

engine = pyttsx3.init()
voices = engine.getProperty('voices')

b_music = ['solang', 'Migos']
pygame.mixer.init()
pygame.mixer.music.load(folder + random.choice(b_music) + '.mp3')
pygame.mixer.music.set_volume(0.10)
pygame.mixer.music.play(-1)

def speak(audio):
    print('Karen:', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Try again')
        pass

    return query


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

class Widget:
    def __init__(self):
       root = Tk()
       root.title('KAREN-My Personal Assistant')
       root.config(background='Blue')
       root.geometry('350x600')
       root.resizable(0, 0)
       root.iconbitmap(r'C:\DOWNLOd\Untitled-1.ico')
       img = ImageTk.PhotoImage(Image.open(r"C:\DOWNLOd\karen-spiderman.jpg"))
       panel = Label(root, image = img)
       panel.pack(side = "bottom", fill = "both", expand = "no")

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click \'Start Listening\' to Give commands')

       userFrame = LabelFrame(root, text="USER", font=('Black ops one', 10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='dodgerBlue', fg='white')
       left2.config(font=("Comic Sans MS", 10, 'bold'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="KAREN", font=('Black ops one', 10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='Red',fg='white')
       left1.config(font=("Comic Sans MS", 10, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='deepSkyBlue', fg='white', command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white', command=root.destroy).pack(fill='x', expand='no')

       
       speak('Hello, I am Karen! What should I do for You?')
       self.compText.set('Hello, I am Karen! What should I do for You?')

       root.bind("<Return>", self.clicked)
       root.mainloop()
    
    def clicked(self):
        print('Working')
        query = myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()


        if 'open my resume' in query:
            self.compText.set('okay')
            speak('okay')
            os.system('C:\\Users\\rishabh\\OneDrive\\Desktop\\karenai\\myresume.pdf')

        elif 'open presentation' in query:
            self.compText.set('okay')
            speak('okay')
            os.system('C:\\Users\\rishabh\\OneDrive\\Desktop\\karenai\\karen.pptx')

        elif 'open youtube' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.google.co.in')
            
        elif 'open linkedin' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('https://www.linkedin.com/feed/')
            
        elif 'open github' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('https://github.com/csharp489?tab=repositories')
            
        elif 'time please' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"MAM,the time is {strTime}")

        elif 'open gmail' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif ('install') in query:
            query = query
            stopwords = ['install']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            speak(('installing '+result))

            os.system('python -m pip install ' + result)

        elif "where is" in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on karishma, I will show you where " + location + " is.")
            os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")



        elif ('sleep mode') in query:
            speak('good night')

            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')


        elif 'shutdown' in query:
            self.compText.set('okay')
            speak('okay')
            os.system('shutdown -s')

        elif ('wi-fi') in query:  
            REMOTE_SERVER = "www.google.com"
            speekmodule.wifi()
            speak('We are connected')


        elif ('.com') in query :
            speak('Opening' + query)        
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")

            webbrowser.get(Chrome).open('http://www.'+query)
            print ('')
            

        elif ('google maps') in query:
            query = query
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            speak(result+'on google maps')


        elif 'turtle program' in query:
            self.compText.set('okay')
            speak('okay')
            os.system("C:\\Users\\rishabh\\OneDrive\\Desktop\\karenai\\mydiag.py\\f5")
            
        elif 'wikipedia' in query:
            self.compText.set('okay')
            speak('okay')
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            self.compText.set(random.choice(stMsgs))
            speak(random.choice(stMsgs))

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'email' in query:
            self.compText.set('Who is the recipient? ')
            speak('Who is the recipient? ')
            recipient = myCommand()
            self.userText.set(recipient)
            recipient = recipient.lower()

            if 'karishma' in recipient:
                try:
                    self.compText.set('What should I say? ')
                    speak('What should I say? ')
                    content = myCommand()
                    self.userText.set(content)
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Email",'Your_Email')
                    server.sendmail('Your_Email', "Recipient_Email", content)
                    server.close()
                    self.compText.set('Email sent!')
                    speak('Email sent!')

                except:
                    self.compText.set('Email sent!')
                    speak('Sorry ' + 'Mam' + '!, I am unable to send your message at this moment!')



        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            self.compText.set('Okay')
            speak('okay')
            self.compText.set('Bye Mam, have a good day.')
            speak('Bye Mam, have a good day.')

        
        
           
        elif 'hello' in query:
            self.compText.set('Hello Mam')
            speak('Hello Mam')
            
        elif 'open code' in query:
            codePath="C:\\Users\\rishabh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open source code' in query:
            self.compText.set('okay')
            speak('okay')
            os.system("C:\\Users\\rishabh\\OneDrive\\Desktop\\karenai\\karen.py")

        elif "open my system jarvis" in query:
            codePath2="C:\\Users\\rishabh\\OneDrive\\Desktop\\LINKS - Mark II.appref-ms"
            os.startfile(codePath2)



        elif 'bye' in query:
            self.compText.set('Bye ' + 'Mam' + ', have a good day.')
            speak('Bye ' + 'Mam' + ', have a good day.')
                                    
        elif 'play music' in query:
            music_folder = 'C:\\DOWNLOd\\'

            music = ['solang', 'Migos']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            
            self.compText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')
            
        else:
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    self.compText.set(results)
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    self.compText.set(results)
                    speak(results)
        
            except:
                speak('I don\'t know Mam! Google is smarter than me!')
                self.compText.set('I don\'t know Sir! Google is smarter than me!')
                webbrowser.open('www.google.com')
                
if __name__ == '__main__':
    greetMe()
    widget = Widget()        
