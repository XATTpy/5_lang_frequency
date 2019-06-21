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


def get_most_frequent_words(word_count, top=25):
    top_words = collections.Counter(word_count).most_common(top)
    return top_words, top


def show_words(word_count):
    top_words, top = get_most_frequent_words(word_count)
    print("{} самых популярных слов в файле:".format(top))
    for word in top_words:
        print(word[0])


def show_top_list():
    try:
        filepath = argv[1]
        text = load_data(filepath)
        words = get_words_from_text(text)
        word_count = get_word_count(words)
        show_words(word_count)
    except (IndexError, IsADirectoryError):
        quit("Введите путь к файлу в качестве аргумента при запуске.")
    except FileNotFoundError:
        quit("Такого файла не существует")


if __name__ == "__main__":
    show_top_list()
