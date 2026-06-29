import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from core.speech.audio_capture import AudioCapture

capture = AudioCapture()

capture.start()

while True:

    pcm = capture.read()

    print(pcm.shape)