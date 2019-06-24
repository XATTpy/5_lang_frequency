import re
from sys import argv
import collections


def load_data(filepath):
    with open(filepath, "r") as text_file:
        return text_file.read()


def get_words_from_text(text):
    words = re.sub(r"[^\w\s]","",text).lower().split()
    return words


def get_count_of_words(words):
    count_of_words = collections.Counter(words)
    return count_of_words


def get_most_frequent_words(count_of_words, toplist_count=10):
    top_words = count_of_words.most_common(toplist_count)
    return top_words, toplist_count


def show_words(count_of_words, top_words, toplist_count):
    print("{} самых популярных слов в файле:".format(toplist_count))
    for word, _ in top_words:
        print(word)


if __name__ == "__main__":
    try:
        filepath = argv[1]
        text = load_data(filepath)
        words = get_words_from_text(text)
        count_of_words = get_count_of_words(words)
        top_words, toplist_count = get_most_frequent_words(count_of_words)
        show_words(count_of_words, top_words, toplist_count)
    except (IndexError, IsADirectoryError):
        quit("Введите путь к файлу в качестве аргумента при запуске.")
    except FileNotFoundError:
        quit("Такого файла не существует")
