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


word_count(r".\test_file.txt") 