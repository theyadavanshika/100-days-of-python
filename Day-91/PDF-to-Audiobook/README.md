# PDF-to-Audiobook Converter

A Python project that converts PDF documents into audiobooks using Google's Gemini Text-to-Speech API.

## Features

- Extracts text from PDF files using PyPDF.
- Splits long text into smaller chunks.
- Converts text into natural-sounding speech using Gemini AI.
- Generates multiple audio chunks in WAV format.
- Combines audio chunks into a single MP3 audiobook.
- Handles missing, empty, and unreadable PDF files.
- Automatically removes old audio chunks before a new conversion.
- Maintains the correct numerical order of audio chunks.

## Technologies Used

- Python
- PyPDF
- Google Gemini API
- Pydub
- FFmpeg
- Python-dotenv

## Project Structure

```text
PDF-to-Audiobook/
│
├── main.py
├── gemini_test.py
├── test_tts.py
├── combine_audio.py
├── .gitignore
└── README.md
```

## Setup Instructions

1. Clone this repository.
2. Install the required packages:

```bash
pip install pypdf google-genai python-dotenv pydub
```

3. Install FFmpeg on your system.
4. Create a `.env` file and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

5. Place your PDF file inside the project folder.
6. Run the TTS script and enter your PDF filename.
7. Combine the generated audio chunks:

```bash
python3 combine_audio.py
```

Your audiobook will be saved as `final_audiobook.mp3`.

## Output

The project generates:
- Individual WAV audio chunks.
- One combined MP3 audiobook.

## What I Learned

Through this project, I practised PDF text extraction, API integration, text chunking, audio processing, file handling, error handling, and working with environment variables.

---

Built as part of the **100 Days of Python** course.
