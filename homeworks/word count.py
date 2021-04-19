'''
Instructions: Please write a program that reads a text file containing some text and for each word in the file counts how many times it
appears. Please note you can use a dictionary structure. Before starting to count words it might be necessary to delete
all punctuation and special symbols (new line, tab etc.) and put all words in lower case.
'''

import re


def word_count(file_path):
    with open(r".\test_file.txt") as Text:
        content = Text.read()

    content = re.sub("[^A-Za-z]", " ", content)

    content = content.lower()
    content = content.split()

    d = {}
    for word in content:
        d[word] = d.get(word, 0) + 1

    freq = []
    for key, value in d.items():
        freq.append((value, key))

    freq.sort()
    freq.reverse()
    print(freq)


word_count(r".\\files\test_file.txt")

# you can test with a .txt file posted on GitHub for testing purposes:
# https://github.com/josecaloca/Python_Summer_2021_2/blob/master/homeworks/test_file