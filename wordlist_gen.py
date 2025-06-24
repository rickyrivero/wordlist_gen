#!/usr/bin/env python3
import os

def prompt_input(prompt, default):
    value = input(f"{prompt} [{default}]: ").strip()
    return value if value else default

def main():
    print("Custom Dictionary Generator for Cracking")
    print("────────────────────────────────────────────────────────────")

    # INPUTS
    base_words_file = prompt_input("Base words file", "base_words.txt")
    output_file = prompt_input("Output file name", "custom_dictionary.txt")

    symbols = prompt_input("Symbols to include (space separated)", "! @ # $ % & * - _").split()
    years_range = prompt_input("Year range (e.g. 2018-2025)", "2018-2025")
    nums = prompt_input("Additional common numbers (e.g. 0 1 123 2024)", "0 1 12 123 2023 2024 2025").split()

    # Process year range
    try:
        start_year, end_year = map(int, years_range.split("-"))
        years = list(map(str, range(start_year, end_year + 1)))
    except Exception:
        print("❌ Error in year format. Use format 2018-2025.")
        return

    # Read base words
    if not os.path.isfile(base_words_file):
        print(f"❌ File not found: {base_words_file}")
        return

    with open(base_words_file, 'r') as f:
        base_words = [w.strip() for w in f if w.strip()]

    # Generate combinations
    print("Generating combinations...")
    combos = set()

    for word in base_words:
        capital = word.capitalize()
        for sym in symbols:
            for year in years + nums:
                combos.update([
                    f"{capital}{year}{sym}", f"{word}{year}{sym}", f"{capital}{sym}{year}", f"{sym}{capital}{year}",
                    f"{word}{sym}{year}", f"{sym}{word}{year}", f"{sym}{capital}{year}", f"{sym}{capital}", f"{capital}{sym}"
                ])

    # Write output file
    with open(output_file, 'w') as out:
        out.write('\n'.join(combos))

    print(f"✅ Dictionary created: {output_file} ({len(combos)} passwords generated)")

if __name__ == "__main__":
    main()
