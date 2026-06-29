from faster_whisper import WhisperModel


class Transcriber:

    def __init__(self):

        print("[Speech] Loading Whisper...")

        self.model = WhisperModel(
            "small",
            device="cuda",
            compute_type="float16",
        )

        print("[Speech] Whisper Ready.")

    def transcribe(self, audio):

        segments, _ = self.model.transcribe(audio)

        result = ""

        for segment in segments:
            result += segment.text

        return result.strip()