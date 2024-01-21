import speech_recognition as sr    #ses tanıma motoru
from gtts import gTTS    # google'nin ses tanıma motoru
from playsound import playsound    




def speak(string):
    tts=gTTS(text=string,lang="tr")
    file="answer.mp3"
    tts.save(file)
    playsound(file)
speak("merhaba nasilsin")


























