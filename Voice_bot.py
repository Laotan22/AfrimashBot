## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

import requests
import speech_recognition as sr  # import the library
import subprocess
from gtts import gTTS
from googletrans import Translator

# sender = input("What is your name?\n")

bot_message = ""
message = ""

translator = Translator()

translation = translator.translate("hello", dest='yo')

r = requests.post(' https://ff5d-2a07-23c0-9-1000-00-8980.ngrok.io/webhooks/telegram/webhook', json={"message": "Hello"})

print("Bot says, ",end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

myobj = gTTS(text=translator.translate(bot_message),lang='hi')
myobj.save("welcome.mp3")
print('saved')
# Playing the converted file
subprocess.call(['cvlc', "welcome.mp3", '--play-and-exit'])

while bot_message != "Bye" or bot_message != 'thanks':

    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            translator = Translator(to_lang='en')
            print("You said : {}".format(translator.translate(message)))

        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
    if len(message) == 0:
        continue
    print("Sending message now...")

    r = requests.post('https://716b-2a07-23c0-8-b000-00-b61b.ngrok.io/webhooks/telegram/webhook',
                      json={"message": translator.translate(message, dest='yo')})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")
    translator = Translator(to_lang='hi')
    myobj = gTTS(text=translator.translate(bot_message))
    myobj.save("welcome.mp3")
    print('saved')
    # Playing the converted file
    subprocess.call(['cvlc', "welcome.mp3", '--play-and-exit'])

