import neuralintents

n = neuralintents.GenericAssistant('intents.json')
n.load_model()

while True:
    inp = input('Say something: ')
    print(n.request(inp))
