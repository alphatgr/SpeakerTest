from gtts import gTTS
import os
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Haider")
    while True:
        s=input("Enter what you want me to speak : ")
        ending="Have a nice day friend, Bye"
        language='en'
        obj=gTTS(text=s,lang=language,slow=False)
        obj.save("Audio.mp3")
        # if s=="Bye":
        #    obj = gTTS(text=s, lang=language, slow=False)
        #    os.system("")
        #    break
        # command=f"say={s}"
        os.system(" Audio.mp3")
