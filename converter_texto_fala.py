import pyttsx3

engine = pyttsx3.init()

engine.say('Olá, como você está?')
engine.say('Em qual linguagem você programa?')

engine.runAndWait()