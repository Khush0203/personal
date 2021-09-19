import pywhatkit as kit
import pyttsx3
speaker = pyttsx3.init()

# kit.sendwhatmsg("+919515384404", "Hey There!",15,22)
# speaker.say("Sending Message")
# speaker.runAndWait()
speaker.say("Enter a songs name")
speaker.runAndWait()
song = input("Enter a songs name: ")
string = "Playing " + song

speaker.say(string)
speaker.runAndWait()
kit.playonyt(song)
