import pyttsx3

if __name__ == '__main__':
    text_to_speech = pyttsx3.init()
    print("Welcome to Robo-Talk 1.0 Created by Abdul Wadood")
    while(True):
        word = input("Enter your command: ")
        if word == 'q':
            break
        text_to_speech.say(word)
        text_to_speech.runAndWait()