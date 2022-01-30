import cores.speak as speak
import neuralintents
from cores.coremodules import core

mappings = {'openminecraft' : core.minecraft, 'addnote':core.addnote, 'removenote':core.removenote, 'listnotes':core.listnotes}
n = neuralintents.GenericAssistant('intents.json', intent_methods=mappings)

n.load_model()

while True:
    text = input('Say something: ').lower()
    speak.say(n.request(text))
