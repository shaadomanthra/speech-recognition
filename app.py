## Microproject to open brower based on audio clip

# import speech library & webbrowser
import speech_recognition as sr
import webbrowser

# create recognizer object, load the file and open the audio
r = sr.Recognizer()
file = sr.AudioFile('open.wav')
with file as source:
    audio = r.record(source)

# use google speech recognition to convert audio to text
text = r.recognize_google(audio)

print(text)                           
