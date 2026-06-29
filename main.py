from core.speech.live_transcriber import LiveTranscriber


def main():

    speech = LiveTranscriber()

    speech.start()


if __name__ == "__main__":
    main()