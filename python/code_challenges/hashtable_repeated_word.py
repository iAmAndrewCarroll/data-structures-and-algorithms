import re
from data_structures.hashtable import Hashtable

def parse_words(input_string):
    return re.findall(r'\b[\w-]+\b', input_string.lower())

def first_repeated_word(input_string):
    words = parse_words(input_string)
    word_count = Hashtable()

    for word in words:
        if word_count.has(word):
            return word
        word_count.set(word, 1)

    return None
