
import pyttsx3
engine = pyttsx3.init()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 196)
engine.setProperty('volume', 2.7)
engine.setProperty('voice', voices[1].id)
engine.say('I love Kush.')
engine.runAndWait()