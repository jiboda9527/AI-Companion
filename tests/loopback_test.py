import sounddevice as sd
import numpy as np

DEVICE = 32

settings = sd.WasapiSettings()

def callback(indata, frames, time, status):

    if status:
        print(status)

    volume = np.abs(indata).mean()

    print(f"Frames:{frames}  Volume:{volume:.6f}")

print("Opening stream...")

try:

    with sd.InputStream(
        device=DEVICE,
        samplerate=48000,
        channels=2,
        dtype="float32",
        callback=callback,
        extra_settings=settings,
    ):

        print("Listening...")

        input()

except Exception as e:

    print(e)