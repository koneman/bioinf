'''
Pattern Matching Problem: Find all occurrences of a pattern in a string.
------------------------
Input: Strings Pattern and Genome.
Output: All starting positions in Genome where Pattern appears as a substring.
'''

import os

comp_dict = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

def read_input(filename):
    data = os.path.abspath(__file__ + "/../../../data")
    file = open(data + "/" + filename, "r")
    return file.read()

def find_pattern(input_dna, pattern):
	index = list()
	for i in range(len(input_dna) - len(pattern)):
		if input_dna[i:i+len(pattern)] == pattern:
			index.append(i)
	return index

def write_to_file(output, idx_arr):
	s=' '.join([str(pos) for pos in idx_arr])
	data = os.path.abspath(__file__ + "/../../../data")
	with open(data + "/" + output, "w") as file:
		file.write(s)

if __name__ == "__main__":
	dna = read_input("Vibrio_cholerae.txt")
	pattern = "CTTGATCAT"
	write_to_file("cholarae_idx.txt", find_pattern(dna, pattern))
