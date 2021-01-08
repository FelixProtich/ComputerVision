import pyttsx3
friend = pyttsx3.init()
print("Welcome to virtual talking friend")
speech = input("Enter Something: ")
friend.say(speech)
friend.runAndWait()
