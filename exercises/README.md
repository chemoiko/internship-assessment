# 🌐 Sunbird Language CLI Tools

This repository contains two Python command-line interface (CLI) tools built to work with the **Sunbird AI APIs** for:
1. 🌍 **Algorithms** 
2. 🎙️ **Audio Transcription** for short speech recordings
3. 🌍 **Text Translation** between local Ugandan languages and English

---

## Getting Started
```
pip install -r requirements.txt
```
### set the environment variables in the .env for the api endpoints and the access token

## 🛠️ Features
### Exercise 1: 
- Implemented the algorithms for the collatz and distinct_numbers for both to pass tests
#### 🔢 Collatz Sequence & Distinct Number Counter

This Python module provides two simple and useful mathematical functions:

1. **`collatz(n)`**: Generates the full Collatz sequence starting from any positive integer.
2. **`distinct_numbers(numbers)`**: Counts how many distinct (unique) numbers exist in a list of integers.

---

## 📘 Function Descriptions

### 1. `collatz(n: int) -> List[int]`

Generates the Collatz sequence for a given positive integer `n`.

#### Algorithm:
- If `n` is even → `n = n / 2`
- If `n` is odd  → `n = 3n + 1`
- Repeat until `n == 1`, collecting all intermediate values.

#### Example:
```python
collatz(3)
# Output: [3, 10, 5, 16, 8, 4, 2, 1]

distinct_numbers([2, 3, 2, 2, 3])
# Output: 2



### 🔤 Exercise 2: Text Translation Tool
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


#### Test
- also contains test file to output the different translations for all pairs though encountered     500  internal error for some translations

```
pytest -s tests/test_translate.py

```


### 🔊 Exercise 3: Audio Transcription Tool
===== Audio Transcription Tool =====
Please provide path to the audio file  (audio length must be less than 5 minutes and must be in .mp3, .wav, .wav, .ogg, .m4a, .aac/)
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


---


