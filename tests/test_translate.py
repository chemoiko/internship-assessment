from dotenv import load_dotenv
from exercises.translate import translate_text, LANGUAGE_CODES
import os
import pytest


"This test file is designed to validate the translation functionality between multiple languages using specific greeting phrases for each language. The primary goal of this test is to verify that the translation service can correctly translate greeting phrases between different source and target languages. This test is useful for ensuring that the translation system works across multiple languages, and that each language pair is correctly handled"

"To run it use pytest -s tests/test_translate.py"
""


load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# Greeting-specific dictionary for each language direction
GREETING_TEXTS = {
    "English": "Hello",  # English to other languages starts with "Hello"
    "Luganda": "Gyebale Ko",  # Luganda to others starts with "Gyebale Ko"
    "Runyankole": "Otya",  # Runyankole to others starts with "what are you afraid of?"
    "Acholi": "Itye",  # Acholi to others starts with "are you there?"
    "Ateso": "Ekitibwa",  # Ateso to others starts with "The lion roars"
    "Lugbara": "awa'difo"  # Lugbara to others starts with "thankyou verymuch"
}

# Generate all source-target language pairs, excluding same-language pairs
language_names = list(LANGUAGE_CODES.keys())
language_pairs = [
    (source, target) for source in language_names for target in language_names if source != target
]


@pytest.mark.parametrize("source_lang,target_lang", language_pairs)
def test_translation_pair_output(source_lang, target_lang):
    print(f"\nTranslating from {source_lang} to {target_lang}...")

    # Select greeting text based on the source language
    source_greeting = GREETING_TEXTS.get(source_lang)

    # Perform translation
    translated = translate_text(
        source_greeting, source_lang, target_lang, ACCESS_TOKEN)

    assert translated is not None and translated.strip(
    ) != "", f"No translation returned for {source_lang} to {target_lang}"

    # Print the result for the specific pair
    print(f"Output for {source_lang} to {target_lang}: {translated}")
