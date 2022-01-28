import neuralintents

n = neuralintents.GenericAssistant('intents.json')

n.train_model()
n.save_model()