import neuralintents
from coremodules import core

mappings = {'openminecraft' : core.minecraft, 'addnote':core.addnote, 'removenote':core.removenote, 'listnotes':core.listnotes}
n = neuralintents.GenericAssistant('intents.json', intent_methods=mappings)

n.train_model()
n.save_model()