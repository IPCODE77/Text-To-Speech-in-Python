# Text To Speech
import pyttsx3,time
engine = pyttsx3.init()
voices = engine.getProperty('voices')

class People:
    def __init__(self,name):
        self.name = name
    def shoutout(self):
        for name in self.name:
            time.sleep(0.3)
            for voice in voices:
                if 'ZIRA' in voice.id:
                    engine.setProperty('voice',voice.id)
                    engine.say(f'Shoutout to {name}')
                    engine.runAndWait()



Namelist = ['Max','Avengers']
Obj = People(Namelist)
Obj.shoutout()
