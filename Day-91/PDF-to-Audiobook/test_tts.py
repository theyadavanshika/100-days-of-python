import os
import glob
import base64
from dotenv import load_dotenv
from google import genai
from main import load_pdf

chunks = load_pdf()

if not chunks:
    print("No text available to convert. Exiting.")
    exit()

load_dotenv()

for file in glob.glob("audio_*.wav"):
    os.remove(file)

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

for index, chunk in enumerate(chunks):

    try:
        interaction = client.interactions.create(
            model="gemini-3.8-flash-tts",
            input=[
                {
                    "type": "user_input",
                    "content": [
                        {
                            "type": "text",
                            "text": chunk,
                            "annotations": [
                                {
                                    "type": "speech_metadata",
                                    "style": "Speak naturally and clearly.",
                                }
                            ],
                        }
                    ],
                }
            ],
            response_format={"type": "audio"},
            generation_config={"speech_config": [{"voice": "Kore"}]},
        )

        audio_data = base64.b64decode(interaction.output_audio.data)

        with open(f"audio_{index + 1}.wav", "wb") as audio_file:
            audio_file.write(audio_data)

        print(f"Audio chunk {index + 1} generated successfully!")

    except Exception as error:
        print(f"Chunk {index + 1} failed: {error}")
        break
