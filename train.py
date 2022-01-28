import neuralintents
from coremodules import core

mappings = {'meme' : core.meme}
n = neuralintents.GenericAssistant('intents.json', intent_methods=mappings)

n.train_model()
n.save_model()