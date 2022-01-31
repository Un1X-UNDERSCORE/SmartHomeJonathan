# Imports
import cores.speak as speak
import neuralintents
from cores.coremodules import core

# Mappings
mappings = {'addnote':core.addnote, 'removenote':core.removenote, 'listnotes':core.listnotes, 'search': core.search}
# Define Neural Networks
n = neuralintents.GenericAssistant('intents.json', intent_methods=mappings)

# Load Neural Network
n.load_model()

# Assistant Loop
while True:
    # Input
    text = input('Say something: ').lower()
    # Say Response
    speak.say(n.request(text))
