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


def show_words(word_count, top_words, top):
    print("{} самых популярных слов в файле:".format(top))
    for word, _ in top_words:
        print(word)


if __name__ == "__main__":
    try:
        filepath = argv[1]
        text = load_data(filepath)
        words = get_words_from_text(text)
        word_count = get_word_count(words)
        top_words, top = get_most_frequent_words(word_count)
        show_words(word_count, top_words, top)
    except (IndexError, IsADirectoryError):
        quit("Введите путь к файлу в качестве аргумента при запуске.")
    except FileNotFoundError:
        quit("Такого файла не существует")
