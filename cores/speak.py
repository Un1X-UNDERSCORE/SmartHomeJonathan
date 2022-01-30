#Config
lang = 'en'
dirr = 'speech/'

#Imports
try:
    from gtts import gTTS
    from hashlib import md5
    from os.path import exists
    from os import mkdir, environ
    from time import sleep
    environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    from pygame.mixer import init, music
    init()
except:
    print("""You have to install the modules: pygame and gtts. Use: 'pip3 install pygame' and 'pip3 install gtts' to install the modules""")
    quit()

#Make dir if not exists
if not exists(dirr):
    mkdir(dirr)

#Say function
def say(text):
    while music.get_busy() == True:
        sleep(0.1)
    print(text)
    if not text or ')' in text or '(' in text:
        return
    #Convert text to hash for file name
    filename = md5(text.encode()).hexdigest()
    #Make path
    path = f"{dirr}{filename}.mp3"
    #Check if file allready exists
    if not exists(path):
        #If not generate the file
        speak = gTTS(text=text, lang=lang, slow=False)
        speak.save(path)
    #Play the sound file
    music.load(path)
    music.play()

#Generate sound file function
def gen(text):
    if not text or ')' in text or '(' in text:
        return
    #Convert text to hash for file name
    filename = md5(text.encode()).hexdigest()
    #Make path
    path = f"{dirr}{filename}.mp3"
    #Check if file allready exists
    if not exists(path):
        #If not generate the file
        speak = gTTS(text=text, lang=lang, slow=False)
        speak.save(path)