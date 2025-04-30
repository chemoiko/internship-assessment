import os
import requests
from pydub import AudioSegment

# ====== Configuration ======
# ← Replace this with your actual token
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwYXRyaWNrY21kIiwiYWNjb3VudF90eXBlIjoiRnJlZSIsImV4cCI6NDg2OTE4NjUzOX0.wcFG_GjBSNVZCpP4NPC2xk6Dio8Jdd8vMb8e_rzXOFc"

# Define supported languages and their codes
LANGUAGE_CODES = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Acholi": "ach",
    "Ateso": "teo",
    "Lugbara": "lgg"
}

# Sunbird ASR API endpoint
SUNBIRD_API_URL = "https://api.sunbird.ai/tasks/asr/transcribe"


def get_audio_duration(file_path):
    try:
        audio = AudioSegment.from_file(file_path)
        return audio.duration_seconds
    except Exception as e:
        print(f"Error reading audio file: {e}")
        return -1


def transcribe_audio(file_path, language_code):
    with open(file_path, "rb") as audio_file:
        files = {"audio": audio_file}
        data = {
            "source_language": language_code,
            "access_token": ACCESS_TOKEN  # Access token included here directly
        }

        print("Transcribing... please wait.")
        response = requests.post(SUNBIRD_API_URL, files=files, data=data)

        if response.status_code == 200:
            result = response.json()
            return result.get("transcription", "No transcription found.")
        else:
            print(
                f"Transcription failed (status code: {response.status_code})")
            print("Details:", response.text)
            return None


def main():
    # Step 1: Ask for audio path
    file_path = input(
        "Please provide path to the audio file (Audio length less than 5 minutes): ").strip()

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

    # Step 3: Choose language
    print("Please choose the target language (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi):")
    for lang in LANGUAGE_CODES:
        print(f"- {lang}")
    chosen_lang = input("Your choice: ").strip()

    if chosen_lang not in LANGUAGE_CODES:
        print("❌ Error: Unsupported language selected.")
        return

    # Step 4: Transcribe
    transcription = transcribe_audio(file_path, LANGUAGE_CODES[chosen_lang])

    if transcription:
        print(f"\n✅ Audio transcription text in {chosen_lang.lower()}:")
        print(transcription)


if __name__ == "__main__":
    main()
