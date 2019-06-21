import re
from sys import argv
import collections


def load_data(filepath):
    with open(filepath, "r") as text_file:
        return text_file.read()


def get_words_from_text(text):
    words = re.sub(r"[^\w\s]","",text).lower().split()
    return words


def get_word_count(words):
    word_count = collections.Counter(words)
    return word_count


def get_most_frequent_words(word_count, top=10):
    top_words = collections.Counter(word_count).most_common(top)
    return top_words, top


def show_top():
    top_words, top = get_most_frequent_words(word_count)
    print("{} самых популярных слов в файле:".format(top))
    for word in top_words:
        print(word[0])


if __name__ == "__main__":
    show_top()
