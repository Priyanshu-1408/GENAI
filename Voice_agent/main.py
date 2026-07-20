import speech_recognition as sr

def main():
    r = sr.Recognizer()  # speech to texxt

    with sr.Microphone() as source: # Mic Access 

        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        print("speak something...")
        audio = r.listen(source)

        print("processing audio... (STT)")
        stt = r.recognize_google(audio)

        print("you said:", stt)

main()        