import mimetypes
import os
import requests
from pydub import AudioSegment
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
SUNBIRD_API_URL = os.getenv("SUNBIRD_TRANSCRIBE_API_URL")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
# Configuration


# Define supported languages and their codes
LANGUAGE_CODES = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Acholi": "ach",
    "Ateso": "teo",
    "Lugbara": "lgg"
}


def get_audio_duration(file_path):
    try:
        audio = AudioSegment.from_file(file_path)
        return audio.duration_seconds
    except Exception as e:
        print(f"Error reading audio file: {e}")
        return -1


def transcribe_audio(file_path, language_code):
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

            print("Transcribing... please wait.")
            response = requests.post(
                SUNBIRD_API_URL,
                headers=headers,
                files=files,
                data=data,
            )

        if response.status_code == 200:
            result = response.json()
            print("Translated Text:", result.get("audio_transcription"))
        else:
            print(
                f"Transcription failed (status code: {response.status_code})")
            print("Details:", response.text)
            return None

    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        return None


def main():
    # Step 1: Ask for audio path
    file_path = input(
        "Please provide path to the audio file (Audio length less than 5 minutes): "
    ).strip()

    if not os.path.exists(file_path):
        print("❌ Error: File does not exist.")
        return

    # Step 2: Check duration
    duration = get_audio_duration(file_path)
    if duration == -1:
        return
    if duration > 300:
        print("❌ Error: Audio is longer than 5 minutes.")
        return

    # Step 3: Choose language using numbers
    print("\nPlease choose the target language:")
    # Convert dictionary to list for indexed access
    languages = list(LANGUAGE_CODES.keys())

    # Display numbered menu
    for index, lang in enumerate(languages, 1):
        print(f"{index}. {lang}")

    # Get user input
    while True:
        try:
            choice = int(input("\nEnter the language of your choice (1-6): "))
            if 1 <= choice <= len(languages):
                chosen_lang = languages[choice - 1]
                break
            else:
                print(
                    f"❌ Please enter a number between 1 and {len(languages)}")
        except ValueError:
            print("❌ Please enter a valid number")

    # Step 4: Transcribe
    transcription = transcribe_audio(file_path, LANGUAGE_CODES[chosen_lang])

    if transcription:
        print(f"\n✅ Audio transcription text in {chosen_lang.lower()}:")
        print(transcription)


if __name__ == "__main__":
    main()
