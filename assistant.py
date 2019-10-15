import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
import vlc
import urllib
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import wikipedia
import random
import playsound
from gtts import gTTS
import wolframalpha
from selenium import webdriver
from time import strftime
greetings=['hello sofia','hi','hi sofia','sofia','hey sofia','hey']
question = ['How are you?', 'How are you doing?']
responses = ['Okay', "I'm fine"]
var1 = ['who made you', 'who created you']
var2 = ['I_was_created_by_Edward_right_in_his_computer.', 'Edward', 'Some_guy_whom_i_never_got_to_know.']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is your name']
cmd1 = ['open browser', 'open google']
cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd4 = ['open youtube', 'i want to watch a video']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing']
cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
cmd8 = ['what is you favourite colour', 'what is your favourite color']
cmd9 = ['thank you']

repfr9 = ['youre welcome', 'glad i could help you']

num = 1
def sofiaResponse1(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("Sofia: ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
    file = str(num)+".mp3"  
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 


def sofiaResponse(audio):
    "speaks audio passed as argument"
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)
def myCommand():
    "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        sofiaResponse1('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        sofiaResponse1('Could not understand your audio, Please try again !')
        command = myCommand();
    return command
def assistant(command):
    "if statements for executing commands"
    

#open subreddit Reddit
    if command in greetings:
        sofiaResponse1('Hi User, I am Sofia and I am your personal voice assistant, Please give a command or say "help me" and I will tell you what all I can do for you.')

        #chatbot
    elif command in question:
        sofiaResponse1('I am fine')
        print('I am fine')
    elif command in var1:
        sofiaResponse1('I was made by sudeesh')
        reply = random.choice(var2)
        print(reply)
    elif command in cmd9:
        print(random.choice(repfr9))
        sofiaResponse1(random.choice(repfr9))
    elif command in cmd7:
        print(random.choice(colrep))
        sofiaResponse1(random.choice(colrep))
        print('It keeps changing every micro second')
        sofiaResponse1('It keeps changing every micro second')
    elif command in cmd8:
        print(random.choice(colrep))
        sofiaResponse1(random.choice(colrep))
        print('It keeps changing every micro second')
        sofiaResponse1('It keeps changing every micro second')
    elif command in cmd2:
        mixer.init()
        mixer.music.load("song.wav")
        mixer.music.play()
    elif command in var4:
        sofiaResponse1('I am a bot, silly')
    elif command in cmd4:
        webbrowser.open('www.youtube.com')
    elif command in cmd6:
        print('see you later')
        sofiaResponse1('see you later')
    elif command in var3:
        print("Current date and time : ")
        print(now.strftime("The time is %H:%M"))
        sofiaResponse1(now.strftime("The time is %H:%M"))
    elif command in cmd1:
        webbrowser.open('www.google.com')
    elif command in cmd3:
        jokrep = random.choice(jokes)
        sofiaResponse1(jokrep)

        
    elif 'open reddit' in command:
            reg_ex = re.search('open reddit (.*)', command)
            url = 'https://www.reddit.com/'
            if reg_ex:
                subreddit = reg_ex.group(1)
                url = url + 'r/' + subreddit
            webbrowser.open(url)
            sofiaResponse1('The Reddit content has been opened for you Sir.')
    elif 'close' in command:
             sofiaResponse1('Bye bye Sir. Have a nice day')
             script=open("assistantwelcome.py", 'r').read()
             exec(script)
             #os.system('python3 /home/pi/Desktop/chatbot')
             sys.exit()
             
    #open website
    elif 'open' in command:
            reg_ex = re.search('open (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.' + domain
                webbrowser.open(url)
                sofiaResponse1('The website you have requested has been opened for you Sir.')
            else:
                pass
    
    #greetings
    elif 'hello' in command:
            day_time = int(strftime('%H'))
            if day_time < 12:
                sofiaResponse1('Hello Sir. Good morning')
            elif 12 <= day_time < 18:
                sofiaResponse1('Hello Sir. Good afternoon')
            else:
                sofiaResponse1('Hello Sir. Good evening')
    elif 'help me' in command:
               print("""
            You can use these commands and I'll help you out:
    1. Open reddit subreddit : Opens the subreddit in default browser.
            2. Open xyz.com : replace xyz with any website name
            3. Send email/email : Follow up questions such as recipient name, content will be asked in order.
            4. Current weather in {cityname} : Tells you the current condition and temperture
            5. Hello
            6. play me a video : Plays song in your VLC media player
            7. change wallpaper : Change desktop wallpaper
            8. news for today : reads top news of today
            9. time : Current system time
            10. top stories from google news (RSS feeds)
            11. tell me about xyz : tells you about xyz
            """)
    #joke
    elif 'joke' in command:
            res = requests.get(
                    'https://icanhazdadjoke.com/',
                    headers={"Accept":"application/json"})
            if res.status_code == requests.codes.ok:
                sofiaResponse1(str(res.json()['joke']))
            else:
                sofiaResponse1('oops!I ran out of jokes')
    #top stories from google news
    elif 'news for today' in command:
            try:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()
                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                for news in news_list[:15]:
                    sofiaResponse1(news.title.text)
            except Exception as e:
                    print(e)
    #current weather
    elif 'current weather' in command:
            reg_ex = re.search('current weather in (.*)', command)
            if reg_ex:
                city = reg_ex.group(1)
                owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                obs = owm.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_status()
                x = w.get_temperature(unit='celsius')
                sofiaResponse1('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
    #time
    elif 'time' in command:
            import datetime
            now = datetime.datetime.now()
            sofiaResponse1('Current time is %d hours %d minutes' % (now.hour, now.minute))
    elif 'email' in command:
        sofiaResponse1('Who is the recipient?')
        recipient = myCommand()
        if 'rajat' in recipient:
            sofiaResponse1('What should I say to him?')
            content = myCommand()
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('asudeesh78@gmail.com', 'sudeesh@1')
            mail.sendmail('sender_email', 'receiver_email', content)
            mail.close()
            sofiaResponse1('Email has been sent successfuly. You can check your inbox.')
        else:
            sofiaResponse1('I don\'t know what you mean!')
    #launch any application
    elif 'launch' in command:
            reg_ex = re.search('launch (.*)', command)
            if reg_ex:
                appname = reg_ex.group(1)
                appname1 = appname+".app"
                subprocess.Popen(["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
                sofiaResponse1('I have launched the desired application')
    #play youtube song
    elif 'play me a song' in command:
            path = '/home/sudeesh/Videos/videos'
            folder = path
            print("folder:"+folder)
            for the_file in os.listdir(folder):
                print("The file:"+the_file)
                file_path = os.path.join(folder, the_file)
                print("The file path:")
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)
            sofiaResponse1('What song shall I play Sir?')
            mysong = myCommand()
            if mysong:
                flag = 0
                url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                response = urllib.request.urlopen(url)
                html = response.read()
                soup1 = soup(html,"lxml")
                url_list = []
                for vid in soup1.findAll(attrs={'class':'yt-uix-tile-link'}):
                    if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                        flag = 1
                        final_url = 'https://www.youtube.com' + vid['href']
                        url_list.append(final_url)
                        url = url_list[0]
                    ydl_opts = {}
                    os.chdir(path)
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])
                        vlc.play(path)
                    if flag == 0:
                      sofiaResponse1('I have not found anything in Youtube ')
    #change wallpaper
    elif 'change wallpaper' in command:
            folder = '/Users/nageshsinghchauhan/Documents/wallpaper/'
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)
            api_key = 'fd66364c0ad9e0f8aabe54ec3cfbed0a947f3f4014ce3b841bf2ff6e20948795'
            url = 'https://api.unsplash.com/photos/random?client_id=' + api_key #pic from unspalsh.com
            f = urllib2.urlopen(url)
            json_string = f.read()
            f.close()
            parsed_json = json.loads(json_string)
            photo = parsed_json['urls']['full']
            urllib.urlretrieve(photo, "/Users/nageshsinghchauhan/Documents/wallpaper/a") # Location where we download the image to.
            subprocess.call(["killall Dock"], shell=True)
            sofiaResponse1('wallpaper changed successfully')
    elif 'search' in command:
        #options = webdriver.ChromeOptions()
        #driver = webdriver.Chrome(chrome_options=options)
        chromedriver = "/home/sudeesh/Downloads/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver)
        driver.get("https://www.google.com/search?q=" +''.join(command))
    #askme anything
    elif 'tell me about' in command:
            reg_ex = re.search('tell me about (.*)', command)
            try:
                if reg_ex:
                    topic = reg_ex.group(1)
                    ny = wikipedia.page(topic)
                    sofiaResponse1(ny.content[:500])
                else:
                    return assistant(myCommand())
            except Exception as e:
                    sofiaResponse(e)
    elif command:
        sofiaResponse1("Sorry i don't know that please try with these")
        print("""
            You can use these commands and I'll help you out:
    1. Open reddit subreddit : Opens the subreddit in default browser.
            2. Open xyz.com : replace xyz with any website name
            3. Send email/email : Follow up questions such as recipient name, content will be asked in order.
            4. Current weather in {cityname} : Tells you the current condition and temperture
            5. Hello
            6. play me a video : Plays song in your VLC media player
            7. change wallpaper : Change desktop wallpaper
            8. news for today : reads top news of today
            9. time : Current system time
            10. top stories from google news (RSS feeds)
            11. tell me about xyz : tells you about xyz
            """)
sofiaResponse1('Hi User, I am Sofia and I am your personal voice assistant, Please give a command or say "help me" and I will tell you what all I can do for you.')
#loop to continue executing multiple commands
while True:
    assistant(myCommand())
