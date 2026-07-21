import pyttsx3

#pyttsx3.speak("Hi how are you")


class TextReader():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate',125)
        self.engine.setProperty('volume',1.0)

    def read(self,toSpeak):
        self.engine.say(toSpeak)
        self.engine.runAndWait()
        self.engine.stop()   

    def get_voices(self):
        voices =self.engine.getProperty('voices')
        for i in voices:
            print(i.gender)
        self.engine.setProperty('voice', voices[1].id)









reader = TextReader()
reader.read("Hi, how are you? My name is Larry")
