def get_num_words(text):
    words = text.split()
    return len(words)

#U3 - shows top 10 words
def get_top_words(text, top_n=10):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n], sum(word_counts.values())

def get_lower_count(text):
    text = text.lower()
    lower = {}
    for char in text:
        if char in lower:
            lower[char] += 1
        else:
            lower[char] = 1
    return lower

def sort_on(dict):
    return dict["num"]

def sort_char_counts(char_dict):
    sorted_chars = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_chars.append({"char": char, "num": count})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars