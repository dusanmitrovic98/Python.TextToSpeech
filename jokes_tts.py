import requests
import json
import pyttsx3

engine = pyttsx3.init()

while True:
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = json.loads(response.text)

    setup = joke["setup"]
    punchline = joke["punchline"]

    engine.say(setup)
    engine.runAndWait()

    engine.say(punchline)
    engine.runAndWait()