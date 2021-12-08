import speech_recognition as sr
import pyttsx3


r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)
r.recognize_google(audio)
r.recognize_google(audio, language='zh')
r.recognize_google(audio, language='ko-KR')


engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()