import speech_recognition as sr
import pyttsx3  # text-to-speech

def initialize_engine():
    engine = pyttsx3.init("sapi5")   # microsoft speech API for voice
    voices = engine.getProperty('voices')  # i get a list of available voices installed on my system.
    engine.setProperty('voice', voices[0].id)  # voice[0] for male and voice[1] for female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)  # speech rate dec by 50 units
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25) # volume inc
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening........")
        r.pause_threshold=1.0
        r.phrase_threshold=0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold=True
        r.operation_timeout=5
        r.non_speaking_duration=0.5
        r.dynamic_energy_adjustment=2
        r.energy_threshold=4000
        r.phrase_time_limit = 10
        ## print(sr.Microphone.list_microphone_names())
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query

#speak("Hello, I'm Nishit")

if __name__ == "__main__":
    while True:
        query = command().lower()
        print(query)
