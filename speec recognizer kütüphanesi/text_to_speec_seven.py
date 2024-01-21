import speech_recognition as sr    #ses tanıma motoru
import pyaudio
from gtts import gTTS
from playsound import playsound    #playsound'un 1.2.2 versiyonunu indirmeniz gerekiyor
import os
from datetime import datetime
import time
import webbrowser

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

def response(voice):
    if "merhaba" in voice:
        speak("sana da merhaba Ömer")
    if "kapan" in voice:
        speak("kapanıyorum iyi günler")
        exit()

    if "hangi gündeyiz" in voice:
        today=time.strftime("%A")
        print(today)
        if today=="Thursday":
            today="perşembe"
        speak(today)
    if "saat kaç" in voice:
        clock=datetime.now().strftime("%H:%M")
        speak(clock)
    if "google'da ara" in voice:
        speak("ne aramamı istersin")
        playsound("dinleme.mp3")
        search=record()
        playsound("kapan.mp3")
        url="https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak(search+ " " + "için google'da bunları buldum")

    if "notumu hesaplar mısın" in voice:
        speak("Tabiki hesaplarım ilk sınav notunu söyleyebilir misin ?")
        not1=record()
        print(not1)
        speak("İkinci sınav notunu söyler misin ?")
        not2=record()

        not1=int(not1)
        not2=int(not2)
        ort=(not1+not2)/2
        speak("Sınav ortalamanız "+ str(ort))


    speak("Başka bir isteğin var mı ?")
    playsound("dinleme.mp3")

speak("Sesli asistana hoşgeldiniz")
i=0
while True:
    if i==0:
        playsound("dinleme.mp3")
        i +=1
    voice=record()
    if voice !='':

        
        voice=voice.lower()
        playsound("kapan.mp3")
        print(voice) 
        response(voice)
        
