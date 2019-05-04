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


def write_to_file(output, s):
	data = os.path.abspath(__file__ + "/../../../data")
	with open(data + "/" + output, "a") as file:
		file.write(s)


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
 Clump Finding Problem:
 ----------------------
 Find patterns forming clumps in a string
 Input: A string Genome, and integers k, L, and t.
 Output: All distinct k-mers forming (L, t)-clumps in Genome.
 
 a k-mer Pattern forms an (L, t)-clump inside a (longer) string Genome if there 
 is an interval of Genome of length L in which this k-mer appears at least t times
'''

'''
 Implement ComputingFrequencies to generate a frequency array.

 Input: A DNA string Text followed by an integer k.
 Output: FrequencyArray(Text).
'''

lex_order = {'A':0, 'C':1, 'G':2, 'T':3}

def pattern_to_num(pattern):
    sum = 0
    sum_idx = 0
    for i in reversed(range(len(pattern))):
        sum += (4**i) * lex_order[pattern[sum_idx]]
        sum_idx += 1
    return sum


def compute_freq(text, k):
    freq_arr = list()

    # initialize the frequency array
    for i in range(4**k):
        freq_arr.append(0)

    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        j = pattern_to_num(pattern)
        freq_arr[j] += 1

    return freq_arr


# def clump(text, k, L, t):
#     # go over this
#     for i in range(L):
#         print(frequent_word(text[0:i+L], k)) 


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

    out_file = "freq_arr_out.txt"
    in_file = "freq_arr.txt"
    
    print('Frequency array: ' + out_file)
    seq = read_input(in_file)
    freq_arr = compute_freq(seq, 7)
    s = ' '.join([str(pos) for pos in freq_arr])
    write_to_file(out_file, s)

