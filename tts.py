from cores.apiai import FifteenAPI

tts_api = FifteenAPI(show_debug=True)

response = tts_api.save_to_file("GLaDOS", "One more test", "tts.wav")