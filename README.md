# 🧠 Wordlist Generator – Custom Dictionary Builder for Password Cracking

Wordlist Generator is a simple but powerful Python CLI tool that helps you generate highly customized wordlists for password cracking.
It's especially useful in red team operations, CTFs, or any brute-force/dictionary attack scenario where generic lists like rockyou.txt just aren’t enough.

By combining base words (such as names, hobbies, or locations) with common patterns like years, symbols, and numbers, this tool creates targeted password combinations tailored to your specific engagement.

## 🔍 Why use this tool?

- 🎯 Targeted attacks – Focus on what matters based on OSINT

- 🔧 Customizable – Input your own words, years, numbers, and symbols

- ⚡ Efficient – Generates thousands of patterns quickly

- 🧪 Ready for cracking – Output file is compatible with tools like Hashcat or John the Ripper

- 💻 Great for red teamers, bug bounty hunters, and pentesters



## Installation

### Run directly with Python

You don’t need to install anything beyond Python 3:

```
git clone https://github.com/your-username/wordlist_gen.git
cd wordlist_gen
python wordlist_gen.py
```

## 🚀 Usage Examples

### Basic usage

Just run the script and follow the prompts:

```
python wordlist_gen.py
```

You’ll be asked to provide:

- Base words file (e.g., `base_words.txt`)

- Output file name (e.g., `custom_dictionary.txt`)

- Symbols to include (e.g., `! @ #`)

- Year range (e.g., `2018-2025`)

- Extra numbers (e.g., `123 2024`)

### Example base words file (base_words.txt)

```
john
maria
football
argentina
```

### Sample prompts and input:

```
Base words file [base_words.txt]:
Output file name [custom_dictionary.txt]:
Symbols to include (space separated) [! @ # $ % & * - _]: ! @
Year range (e.g. 2018-2025) [2018-2025]: 2020-2024
Additional common numbers (e.g. 0 1 123 2024) [0 1 12 123 2023 2024 2025]: 123 321
```

### Output preview (custom_dictionary.txt):

```
John2020!
john2020!
John!2020
!John2020
john!2020
!john2020
!John2020
!John
John!
...
```

This list will contain hundreds or thousands of combinations depending on your input — ready to use in password cracking tools.
