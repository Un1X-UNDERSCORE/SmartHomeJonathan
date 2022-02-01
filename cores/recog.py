import micvadstreaming as micvadstreaming

class ARGS:
    device=None
    file=None
    model='/home/jonathan/spam/bruh/deepspeech-0.9.3-models.tflite'
    nospinner=False
    rate=16000
    savewav=None
    scorer='/home/jonathan/spam/bruh/deepspeech-0.9.3-models.scorer'
    vad_aggressiveness=3

micvadstreaming.main(ARGS)
