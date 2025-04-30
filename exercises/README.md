# 🌐 Sunbird Language CLI Tools

This repository contains two Python command-line interface (CLI) tools built to work with the **Sunbird AI APIs** for:

1. 🌍 **Text Translation** between local Ugandan languages and English
2. 🎙️ **Audio Transcription** for short speech recordings

---

## 🛠️ Features
### Exercise 1: 
- Implemented the algorithms for the collatz and distinct_numbers for both to pass tests



### 🔤 Exercise 2: Transcription Tool
- Translate text between:
  - English (`eng`)
  - Luganda (`lug`)
  - Runyankole (`nyn`)
  - Acholi (`ach`)
  - Ateso (`teo`)
  - Lugbara (`lgg`)
- Interactive CLI selection for source and target language
- Secure API authentication with `.env` tokens

## Test
- also contains test file to output the different translations for all pairs though encountered     500  internal error for some translations
- pytest -s tests/test_translate.py

### 🔊 Exercise 3: Audio Transcription Tool
- Supports audio files (`.mp3`, `.wav`, `.ogg`, `.m4a`, `.aac`)
- Detects file MIME types
- Verifies audio duration (max: **5 minutes**)
- Sends to Sunbird’s transcribe API and displays transcription result

---

## 📁 Project Structure

