#!/usr/bin/python
import os
import csv
import random


def cost(s1, s2, costMatrix):  # takes in two characters and finds their cost.
    return(int(next(item for item in costMatrix if item['key'] == s1)[s2]))


def create_random_sequences(size):
    # create a sequence pair of a given length
    seq1 = ""
    seq2 = ""
    generated = 0
    choices = ['G', 'A', 'T', 'C']
    while (generated < size):
        seq1 += choices[random.randint(0, 3)]
        seq2 += choices[random.randint(0, 3)]
        generated = generated + 1
    return(seq1+','+seq2)


def generate_sequences():
    # make sure directory exists for generated sequences
    if not os.path.exists("random_sequences"):
        os.makedirs("random_sequences")
    sizes = [500, 1000, 2000, 4000, 5000]
    file_prefix = "random_sequences/input_"
    file_extension = ".txt"
    # generate 10 random pairs of sequences for each size
    for size in sizes:
        output = open(file_prefix+str(size)+file_extension, "w")
        generated = 0
        while (generated < 10):
            output.write("%s\n" % create_random_sequences(size))
            generated = generated + 1
        output.close()


def parse_sequences(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)
    return(lines)


def parse_weight_matrix(file_path):
    # parse csv into lines
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)
    # parse lines into dictionary
    weights = []
    for i, src in enumerate(lines[0]):
        if (src != '*'):
            weights_row = {}
            weights_row["key"] = src
            for dst in lines[1:]:
                weights_row[dst[0]] = dst[i]
            weights.append(weights_row)
    return(weights)


# traceback to find optimal sequences
def traceback_sequences(m, n, seq1, seq2, opt_results):
    x = opt_results[m][n][1]
    i = m
    j = n
    opt_seq1 = ""
    opt_seq2 = ""
    while (x > 0):
        # 1 or 3 both do column
        if (x == 1 or x == 3):
            # account for base cases to not go out of range
            if(j <= 0):
                opt_seq2 = '-' + opt_seq2
            # if not base case, align
            else:
                opt_seq2 = seq2[j-1] + opt_seq2
                j = j - 1
        # 1 or 2 both do row
        if (x == 1 or x == 2):
            # account for base cases to not go out of range
            if(i <= 0):
                opt_seq1 = '-' + opt_seq1
            # if not base case, align
            else:
                opt_seq1 = seq1[i-1] + opt_seq1
                i = i - 1
        if (x == 2):
            opt_seq2 = '-' + opt_seq2
        if (x == 3):
            opt_seq1 = "-" + opt_seq1
        # update x
        x = opt_results[i][j][1]
    # return tuple of results
    return (opt_seq1, opt_seq2)
