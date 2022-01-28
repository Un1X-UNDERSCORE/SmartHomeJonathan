import speak
import neuralintents
from coremodules import core

mappings = {'meme' : core.meme}
n = neuralintents.GenericAssistant('intents.json', intent_methods=mappings)

n.load_model()

while True:
    text = input('Say something: ')
    speak.say(n.request(text))
