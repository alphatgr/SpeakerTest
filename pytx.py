import pyttsx3
text_speech=pyttsx3.init()
s=input("Enter what you want me to speak : ")
text_speech.say(s)
text_speech.runAndWait()