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

def write_to_file(output, s):
	data = os.path.abspath(__file__ + "/../../../data")
	with open(data + "/" + output, "a") as file:
		file.write(s)

def reverse(s):
	return s[::-1]

def rev_complement(input_dna):
	dna_list = list(input_dna)
	return reverse("".join(comp_dict.get(nuc, nuc) for nuc in dna_list))

if __name__ == "__main__":
	dna = read_input("dna_seq.txt")
	comp_dna = rev_complement(dna)
	write_to_file("rev_comp.txt", comp_dna)
