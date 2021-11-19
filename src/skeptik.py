### SKEPTIK
import speech_recognition as sr
from playsound import playsound
import random
# initialize the recognizer
r = sr.Recognizer()
## RECORDING FROM MIC
with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("===============================================================")
    print("===============================================================")
    print("ASK QUESTION...")
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)
    print("ANSWER...")
    _data = r.record(source, duration=8)
    print("Recognizing...")
    text = r.recognize_google(_data)
    print(text)
    
    playsound("../assets/sus.mp3")
    result = random.choice(["true", "false"])   

    true_sound = ['Audio Track-10.mp3', 'Audio Track-3.mp3', 'Audio Track-5.mp3', 'Audio Track-7.mp3', 'Audio Track-9.mp3', 'Audio Track-2.mp3', 'Audio Track-4.mp3', 'Audio Track-6.mp3', 'Audio Track-8.mp3', 'Audio Track.mp3']
    false_sound = ['Audio Track-11.mp3', 'Audio Track-3-2.mp3', 'Audio Track-5-2.mp3', 'Audio Track-4-2.mp3', 'Audio Track-6-2.mp3']
	

    if "true" in text or "false" in text:
        if result == 'true':
            playsound(f"../assets/Game-show-correct-answer.mp3")
            sound = random.choice(true_sound)      
            playsound(f"../assets/{sound}")
        elif result == 'false':
            playsound(f"../assets/Wrong-answer-sound-effect.mp3")
            sound = random.choice(false_sound)      
            playsound(f"../assets/{sound}")
    else:
        sound = 'Audio Track-2-2.mp3'
        playsound(f"../assets/{sound}")