from pydub import AudioSegment
import glob

audio_files = sorted(
    glob.glob("audio_*.wav"), key=lambda file: int(file.split("_")[1].split(".")[0])
)

combined_audio = AudioSegment.empty()

for file in audio_files:
    audio = AudioSegment.from_wav(file)
    combined_audio += audio

combined_audio.export("final_audiobook.mp3", format="mp3")

print("Audiobook created successfully!")
