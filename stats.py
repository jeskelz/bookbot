# accepts the text from the book as a string, and returns the number of words in the string    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def sort_characters(counts_dict):
    # Convert to a list of {"char": x, "num": y} dicts
    sorted_list = []
    for char, count in counts_dict.items():
        if char.isalpha():  # Only include alphabetic characters
            sorted_list.append({"char": char, "num": count})
    
    # Sort from greatest to least using a helper function
    def sort_on(item):
        return item["num"]

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


# Top 10 Most Common Words
from collections import Counter
import re

def get_top_words(text, n=10):
    words = re.findall(r'\b\w+\b', text.lower())  # Clean and lowercase words
    word_counts = Counter(words)
    return word_counts.most_common(n)

