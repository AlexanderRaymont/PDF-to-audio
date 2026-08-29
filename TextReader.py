import pyttsx3

#pyttsx3.speak("Hi how are you")


class TextReader():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate',125)
        self.engine.setProperty('volume',1.0)
        self.contentToRead = None

    def set_text_to_read(self,content):
        self.contentToRead = content

    def read(self,toSpeak):
        self.engine.say(toSpeak)
        self.engine.runAndWait()
        self.engine.stop()   

    def read_content(self):
        if(self.contentToRead == None):
            print("ERROR: NOTHING TO READ")
            exit(0)
        for i in self.contentToRead:
            self.engine.say(i)
            self.engine.runAndWait()
            self.engine.stop()

    def get_voices(self):
        voices =self.engine.getProperty('voices')
        for i in voices:
            print(i.languages)
        self.engine.setProperty('voice', voices[1].id)









reader = TextReader()
reader.read("Hi, how are you? My name is Larry")
reader.get_voices()