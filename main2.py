import pyttsx3
if __name__ == '__main__':
    engine=pyttsx3.init()
    print("Welcome to RoboSpeaker 1.1. Created by Haider")
    while True:
        s=input("Enter what you want me to speak : ")
        if s=="Bye" or s=="bye" or s=="BYE":
            engine.say("Have a nice day friend, Bye")
            engine.runAndWait()
        break
        engine.say(s)
        engine.runAndWait()