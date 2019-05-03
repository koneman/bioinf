'''
 Frequent Words Problem
 ----------------------
 Input: A string Text and an integer k.
 Output: All most frequent k-mers in Text.

 k-mer - string of length k
'''

import os
import time


def read_input(filename):
    data = os.path.abspath(__file__ + "/../../../data")
    file = open(data + "/" + filename, "r")
    return file.read()


def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count


def frequent_word(text, k):
    freq_patterns = set()
    count = list()

    for i in range(len(text) - k):
        pattern = text[i:i+k]
        count.append(pattern_count(text, pattern))

    maxCount = max(count)

    for i in range(len(text) - k):
        if count[i] == maxCount:
            freq_patterns.add(text[i:i+k])

    return freq_patterns


'''
 Clump Finding Problem
 ---------------------
 find patterns forming clumps in a string
 Input: a string genome and integers k(length of pattern)
'''


if __name__ == "__main__":
    # text = read_input("Vibrio_cholerae.txt")
    text = read_input("test.txt")
    pattern = "CGC"

    count = pattern_count(text, pattern)
    print("----------------------")
    print("Count of " + pattern + ": "+ str(count))
    print("----------------------")

    k = 3
    tic = time.time()
    frequent_words = frequent_word(text, k)
    toc = time.time()
    print("Frequent Words: ")
    print(frequent_words)

    print("time elapsed: " + str(toc - tic))
    print("----------------------")
