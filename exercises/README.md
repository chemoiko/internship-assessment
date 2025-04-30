# 🌐 Sunbird Language CLI Tools

This repository contains Python command-line interface (CLI) tools built to work with the **Sunbird AI APIs** for:

1. 🔢 **Algorithms** - Simple mathematical functions
2. 🌍 **Text Translation** - Between local Ugandan languages and English
3. 🎙️ **Audio Transcription** - For short speech recordings

## 📋 Getting Started

```bash
pip install -r requirements.txt
```

Set the environment variables in the `.env` file for the API endpoints and the access token:

```
SUNBIRD_API_URL=https://api.sunbird.ai/...
SUNBIRD_API_TOKEN=your_access_token_here
```

## 🛠️ Features

### Exercise 1: Mathematical Algorithms

#### 🔢 Collatz Sequence & Distinct Number Counter

This module provides two mathematical functions that pass all tests:

1. **`collatz(n)`**: Generates the full Collatz sequence starting from any positive integer
2. **`distinct_numbers(numbers)`**: Counts how many distinct (unique) numbers exist in a list of integers

##### Function Descriptions

**`collatz(n: int) -> List[int]`**

Generates the Collatz sequence for a given positive integer `n`.

Algorithm:
- If `n` is even → `n = n / 2`
- If `n` is odd  → `n = 3n + 1`
- Repeat until `n == 1`, collecting all intermediate values

Example:
```python
collatz(3)
# Output: [3, 10, 5, 16, 8, 4, 2, 1]
```

**`distinct_numbers(numbers: List[int]) -> int`**

Counts the number of unique values in a list of integers.

Example:
```python
distinct_numbers([2, 3, 2, 2, 3])
# Output: 2
```

### 🔤 Exercise 2: Text Translation Tool

The translation tool enables translation between English and various Ugandan languages.

#### Example Usage:

```
Choose the source language:
1. English
2. Luganda
3. Ruyankore
...

Enter number: 1

Choose the target language:
1. English
2. Luganda
3. Ruyankore
...

Enter number: 2

Enter the text to translate from English to Luganda:
Hello, how are you?

Translated text in Luganda:
Gyebale ko, oli otya?
```

#### Testing

The repository includes a test file to output translations for all language pairs, though some translations may encounter 500 internal errors:

```bash
pytest -s tests/test_translate.py
```

### 🔊 Exercise 3: Audio Transcription Tool

Transcribe audio files in various Ugandan languages.

#### Example Usage:

```
===== Audio Transcription Tool =====
Please provide path to the audio file (audio length must be less than 5 minutes and must be in .mp3, .wav, .ogg, .m4a, .aac/)
> ./sample_audio.mp3

Audio duration: 1m 30s

Please choose the target language:
1. English
2. Luganda
3. Ruyankore
...

Enter language number or name: 2

Transcribing audio in Luganda (code: lug)...

✅ Transcription complete!
==================================================
Gyebale ko, twagala okwogera ku nsonga za leero.
==================================================
```

## 📄 License

[License information]

## 🤝 Contributing

[Contribution guidelines]

## 📞 Support

[Support information]