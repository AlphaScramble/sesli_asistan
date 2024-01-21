import speech_recognition as sr    #ses tanıma motoru
import pyaudio
from gtts import gTTS
from playsound import playsound    #playsound'un 1.2.2 versiyonunu indirmeniz gerekiyor
import os



def speak(string):
    tts=gTTS(text=string,lang="tr")
    file="answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)



speak("merhaba nasilsin")