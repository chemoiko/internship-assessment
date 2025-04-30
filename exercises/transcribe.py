import mimetypes
import os
import requests
from pydub import AudioSegment
from dotenv import load_dotenv


"""
Audio Transcription Tool
=======================

A command-line application that transcribes audio files into text using the Sunbird API.
This tool supports multiple African languages including English, Luganda, Runyankole, 
Acholi, Ateso, and Lugbara.

Note:
-----
Audio files must be less than 5 minutes in length for optimal transcription.
"""


# Load environment variables
load_dotenv()

# Configuration
SUNBIRD_API_URL = os.getenv("SUNBIRD_TRANSCRIBE_API_URL")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Validate required environment variables
if not SUNBIRD_API_URL:
    raise ValueError(
        "SUNBIRD_TRANSCRIBE_API_URL environment variable is missing")

# Define supported languages and their codes
LANGUAGE_CODES = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Acholi": "ach",
    "Ateso": "teo",
    "Lugbara": "lgg"
}
LANGUAGES = list(LANGUAGE_CODES.keys())  # Use dictionary keys as language list


def get_audio_duration(file_path):
    """Get audio file duration in seconds."""
    try:
        audio = AudioSegment.from_file(file_path)
        duration = audio.duration_seconds
        print(f"Audio duration: {int(duration//60)}m {int(duration%60)}s")
        return duration
    except Exception as e:
        print(f"Error reading audio file: {e}")
        return -1


def get_language_choice():
    """Get user's language choice with improved input handling."""
    print("\nPlease choose the target language:")

    # Display numbered menu
    for index, lang in enumerate(LANGUAGES, 1):
        print(f"{index}. {lang}")

    while True:
        choice = input("\nEnter language number or name: ").strip()

        # Check if input is a valid language name
        if choice in LANGUAGES:
            return choice

        # Check if input is a valid number
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(LANGUAGES):
                return LANGUAGES[choice_num - 1]
            else:
                print(
                    f"❌ Please enter a number between 1 and {len(LANGUAGES)}")
        except ValueError:
            print(
                f"❌ Please enter a valid number or one of: {', '.join(LANGUAGES)}")


def transcribe_audio(file_path, language_code):
    """Transcribe audio file using Sunbird API."""
    try:
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }

        data = {
            "language": language_code,
            "adapter": language_code,
            "whisper": True
        }

        # Dynamically get the MIME type
        mime_type, _ = mimetypes.guess_type(file_path)

        with open(file_path, "rb") as audio_file:
            files = {
                "audio": (
                    os.path.basename(file_path),
                    audio_file,
                    mime_type or "application/octet-stream"
                )
            }

            print(f"Transcribing... this may take a moment depending on audio length.")
            response = requests.post(
                SUNBIRD_API_URL,
                headers=headers,
                files=files,
                data=data,
            )

        if response.status_code == 200:
            result = response.json()
            transcription = result.get("audio_transcription")
            if not transcription:
                print("⚠️ Response received but no transcription found in response.")
                print(f"API response: {result}")
                return None
            return transcription
        else:
            print(
                f"❌ Transcription failed (status code: {response.status_code})")
            print("Details:", response.text)
            return None

    except Exception as e:
        print(f"❌ Error during transcription: {str(e)}")
        return None


def main():
    """Main application entry point."""
    print("===== Audio Transcription Tool =====")

    if not ACCESS_TOKEN:
        print("❌ Error: Access token is missing. Please check your .env file.")
        return

    # Step 1: Ask for audio path
    file_path = input(
        "Please provide path to the audio file  (audio length must be less than 5 minutes and must be in .mp3, .wav, .wav, .ogg, .m4a, .aac/): "
    ).strip()

    if not os.path.exists(file_path):
        print("❌ Error: File does not exist.")
        return

    # Step 2: Check duration
    duration = get_audio_duration(file_path)
    if duration == -1:
        return
    if duration > 300:
        print("❌ Error: Audio is longer than 5 minutes (300 seconds).")
        return

    # Step 3: Choose language
    chosen_lang = get_language_choice()
    language_code = LANGUAGE_CODES[chosen_lang]

    print(f"\nTranscribing audio in {chosen_lang} (code: {language_code})...")

    # Step 4: Transcribe
    transcription = transcribe_audio(file_path, language_code)

    if transcription:
        print(f"\n✅ Transcription complete!")
        print("=" * 50)
        print(transcription)
        print("=" * 50)
    else:
        print("❌ Transcription failed or returned empty result.")


if __name__ == "__main__":
    main()
