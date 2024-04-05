import whisper

model = whisper.load_model("base")


def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]


if __name__ == "__main__":
    print(
        transcribe_audio(
            "/home/evans/Documents/Work/Gladys/experiments/gladys-multimodal-experiment/speech/speaker_rec_training_data/evans/evans 1.wav"
        )
    )
