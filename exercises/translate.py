import requests
from dotenv import load_dotenv
import os

load_dotenv()
# Add language code mapping
url = os.getenv("SUNBIRD_TRANSLATE_API_URL")
access_token = os.getenv("ACCESS_TOKEN")

LANGUAGE_CODES = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Acholi": "ach",
    "Ateso": "teo",
    "Lugbara": "lgg"
}
LANGUAGES = list(LANGUAGE_CODES.keys())  # Use dictionary keys as language list


def get_language_input(prompt):
    print(prompt)
    for i, lang in enumerate(LANGUAGES, 1):
        print(f"{i}. {lang}")
    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(LANGUAGES):
                return LANGUAGES[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(LANGUAGES)}")
        except ValueError:
            print("Please enter a valid number")

# translate function


def translate_text(text, source_lang, target_lang, access_token):

    # Convert language names to codes
    source_code = LANGUAGE_CODES.get(source_lang)
    target_code = LANGUAGE_CODES.get(target_lang)

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "source_language": source_code,
        "target_language": target_code,
        "text": text
    }

    try:
        print("Sending payload:", payload)  # Debug print
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        # print(f"Status Code: {response.status_code}")
        # print(f"Response: {response.text}")

        return response.json().get("output", {}).get("translated_text")
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        print(
            f"Response content: {response.text if 'response' in locals() else 'No response'}")
        return None


def main():

    if not access_token:
        print("Error: Access token is empty")
        return

    print(f"Token length: {len(access_token)}")  # Debug print

    source_lang = get_language_input("Choose the source language:")
    target_lang = get_language_input("Choose the target language:")

    if source_lang == target_lang:
        print("Source and target languages cannot be the same.")
        return

    text = input(
        f"Enter the text to translate from {source_lang} to {target_lang}:\n")

    translated = translate_text(text, source_lang, target_lang, access_token)

    if translated:
        print(f"\nTranslated text in {target_lang}:\n{translated}")
    else:
        print("Translation failed. Please check the error messages above.")


if __name__ == "__main__":
    main()
