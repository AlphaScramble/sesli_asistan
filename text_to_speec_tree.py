import speech_recognition as sr    #ses tanıma motoru
import pyaudio
from gtts import gTTS
from playsound import playsound    #playsound'un 1.2.2 versiyonunu indirmeniz gerekiyor
import os


r=sr.Recognizer()


def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio=r.listen(source)
        voice=""

        try:
            voice= r.recognize_google(audio,language="tr")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("sistem çalışmıyor")
        return voice
    

def speak(string):
    tts=gTTS(text=string,lang="tr")
    file="answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)



speak("merhaba nasilsin gardaş")

voice=record()

if voice !='':
    voice=voice.lower()
    print(voice) 

if "merhaba" in voice:
    speak("Sana da merhaba Ömer")

    

