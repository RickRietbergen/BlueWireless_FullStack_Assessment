import re
from collections import Counter

def word_count(input_file, output_file):
    """
    Reads input_file, counts occurrences of each word (case-insensitive),
    and writes results to output_file in the format: word: count
    Words are sequences of alphanumeric characters and underscores.
    """
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        raise

    words = re.findall(r"\b\w+\b", text.lower())
    counts = Counter(words)

    # Sort results alphabetically by word
    with open(output_file, "w", encoding="utf-8") as out:
        for word in sorted(counts):
            out.write(f"{word}: {counts[word]}\n")

if __name__ == "__main__":
    word_count("python_app_dev_test/src/input.txt", "python_app_dev_test/src/output.txt")
