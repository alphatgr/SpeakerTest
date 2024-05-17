import os
import pyttsx3
engine=pyttsx3.init()
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Haider Abbas")
    while True:
        s=input("Enter what you want me to speak : ")
        if s=="Bye":
           os.system("say'Have a nice day friend, Bye'")
           break
        command=f"say={s}"
        os.system(command)
