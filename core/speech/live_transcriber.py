from core.speech.audio_capture import AudioCapture
from core.speech.transcriber import Transcriber


class LiveTranscriber:

    def __init__(self):

        self.audio = AudioCapture()

        self.whisper = Transcriber()

    def start(self):

        self.audio.start()

        print("[Speech] Listening...")

        while True:

            pcm = self.audio.read()

            text = self.whisper.transcribe(pcm)

            if text:

                print(text)