import speak
import neuralintents

n = neuralintents.GenericAssistant('intents.json')

n.load_model()

while True:
    text = input('Say something: ')
    speak.say(n.request(text))