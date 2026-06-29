import queue
import numpy as np
import pyaudiowpatch as pyaudio


class AudioCapture:

    def __init__(
        self,
        device_name="SteelSeries Sonar - Media",
        sample_rate=16000,
        channels=1,
        chunk=1600,
    ):
        self.device_name = device_name
        self.sample_rate = sample_rate
        self.channels = channels
        self.chunk = chunk

        self.audio = pyaudio.PyAudio()

        self.stream = None

        self.queue = queue.Queue()

        self.device_index = None

    def start(self):

        self.device_info = self._find_device()

        print(self.device_info)

        self._open_stream()

    def stop(self):

        if self.stream:

            self.stream.stop_stream()
            self.stream.close()

        self.audio.terminate()

    def read(self):

        return self.queue.get()

    def _find_device(self):

        print("[Audio] Searching WASAPI Loopback...")

        for device in self.audio.get_loopback_device_info_generator():

            print(device["index"], device["name"])

            if self.device_name in device["name"]:

                print(f"[Audio] Found: {device['name']}")

                return device

        raise RuntimeError(
            f"Cannot find loopback device: {self.device_name}"
        )

    def _open_stream(self):

        self.stream = self.audio.open(

            format=pyaudio.paInt16,

            channels=8,

            rate=int(self.device_info["defaultSampleRate"]),

            input=True,

            input_device_index=self.device_info["index"],

            frames_per_buffer=self.chunk,

            stream_callback=self._callback,

        )

        self.stream.start_stream()

        print("[Audio] Loopback started.")

    def _callback(self, in_data, frame_count, time_info, status):

        audio = np.frombuffer(
            in_data,
            dtype=np.int16
        )

        self.queue.put(audio)

        return (
            None,
            pyaudio.paContinue
        )