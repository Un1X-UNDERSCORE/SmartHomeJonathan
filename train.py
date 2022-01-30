# Imports
import neuralintents
from cores.coremodules import core

# Mappings
mappings = {'addnote':core.addnote, 'removenote':core.removenote, 'listnotes':core.listnotes}
# Define neural network
n = neuralintents.GenericAssistant('intents.json', intent_methods=mappings)

# Train and save model
n.train_model()
n.save_model()