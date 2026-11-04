import os
import base64
from dotenv import load_dotenv
from google import genai
from main import chunks

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Connect to Gemini
client = genai.Client(api_key=API_KEY)

# Generate speech
for index, chunk in enumerate(chunks):

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

audio_data = base64.b64decode(interaction.output_audio.data)

with open("gemini_test.wav", "wb") as audio_file:
    audio_file.write(audio_data)

print("Audio generated successfully!")
