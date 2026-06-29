from faster_whisper import WhisperModel


class LiveTranscriber:
    """
    AI Companion Speech Engine
    """

    def __init__(self):

        print("[Speech] Loading Whisper model...")

        self.model = WhisperModel(
            "small",
            device="cuda",
            compute_type="float16"
        )

        print("[Speech] Whisper loaded.")

    def start(self):

        print("[Speech] Start listening...")

    def stop(self):

        print("[Speech] Stop.")