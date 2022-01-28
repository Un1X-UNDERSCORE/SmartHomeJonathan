<<<<<<< HEAD
import speak
import neuralintents

n = neuralintents.GenericAssistant('intents.json')

n.load_model()

while True:
    text = input('Say something: ')
    speak.say(n.request(text))
=======
from speak import say

while True:
    text = input('What to say: ')
    say(text)
>>>>>>> 2dc558c2cdbd03122e50445ca999288beef48e87
