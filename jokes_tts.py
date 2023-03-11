import requests
import json
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Female voice. Remove it for default male voice.

while True:
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = json.loads(response.text)

    setup = joke["setup"]
    punchline = joke["punchline"]

    engine.say(setup)
    engine.runAndWait()

    engine.say(punchline)
    engine.runAndWait()