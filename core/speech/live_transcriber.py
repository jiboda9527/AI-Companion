import soundcard as sc
from faster_whisper import WhisperModel
import numpy as np

class LiveTranscriber:

    def __init__(self):

        print("[Speech] Loading Whisper model...")

        self.model = WhisperModel(
            "small",
            device="cuda",
            compute_type="float16"
        )

        print("[Speech] Whisper loaded.")

    def start(self):

        speakers = sc.all_speakers()

        speaker = next(
            s for s in speakers
            if "SteelSeries Sonar - Media" in s.name
        )

        print(f"Using: {speaker.name}")

        with speaker.recorder(samplerate=16000) as mic:

            print("Listening...")

            while True:

                data = mic.record(numframes=16000)

                volume = np.abs(data).mean()

                print(f"Volume: {volume:.5f}")

    def stop(self):
        print("[Speech] Stop.")