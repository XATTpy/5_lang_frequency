import re
from sys import argv
import collections


def load_data(filepath):
    with open(filepath, "r") as text:
        return text.read()


def get_words_from_text(text):
    words = re.sub(r"[^\w\s]","",text).lower().split()
    return words


def get_word_count(words):
    word_count = collections.Counter()
    for word in words:
        word_count[word] += 1
    return word_count


def get_most_frequent_words(word_count):
    top_ten = []
    for _ in range(10):
        word = max(word_count, key=word_count.get)
        top_ten.append(word)
        word_count.pop(word)
    return top_ten


def show_top_ten():
    try:
        filepath = "git.txt"
        text = load_data(filepath)
        words = get_words_from_text(text)
        word_count = get_word_count(words)
        print(get_most_frequent_words(word_count))
    except (IndexError, IsADirectoryError):
        quit("Введите путь к файлу в качестве аргумента при запуске.")
    except FileNotFoundError:
        quit("Такого файла не существует")


if __name__ == "__main__":
    show_top_ten()
