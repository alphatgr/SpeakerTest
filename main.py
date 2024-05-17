import pyttsx3
if __name__ == '__main__':
    
    engine=pyttsx3.init()
    engine.say("Welcome to the TEXT TO SPEECH CONVERTER. Created by Haider Abbas " + "To close the app you can type Exit or Bye")
    print("Welcome to the TEXT TO SPEECH CONVERTER. Created by Haider Abbas. " + "\n" + "To close the app you can type Exit or Bye")
    engine.runAndWait()
    
    # RATE
    rate=engine.getProperty('rate')
    engine.setProperty('rate',120)
    
    # VOICE
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice',voices[1].id)
    
    while True:
        s=input("Enter what you want me to say : ")
        if s=="BYE" or s=="bye" or s=="Bye" or s=="exit" or s=="Exit" or s=="EXIT":
            engine.say("Thanks for using me. Have a nice day friend!")
            engine.runAndWait()
            break
        engine.say(s)
        engine.runAndWait()