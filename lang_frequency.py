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
    word_count = collections.Counter()
    for word in words:
        word_count[word] += 1
    return word_count


def get_most_frequent_words(word_count, top=69):
    top_ten = []
    for _ in range(top):
        word = max(word_count, key=word_count.get)
        top_ten.append(word)
        word_count.pop(word)
    return top_ten, top


def show_top():
    try:
        filepath = argv[1]
        text = load_data(filepath)
        words = get_words_from_text(text)
        word_count = get_word_count(words)

        word_count, top = get_most_frequent_words(word_count)
        print("{} самых популярных слов в файле:".format(top))
        for word in word_count:
            print(word)

    except (IndexError, IsADirectoryError):
        quit("Введите путь к файлу в качестве аргумента при запуске.")
    except FileNotFoundError:
        quit("Такого файла не существует")


if __name__ == "__main__":
    show_top()
