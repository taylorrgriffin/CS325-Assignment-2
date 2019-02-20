#!/usr/bin/python
import os
import csv
import random

def create_random_sequences(size):
    # create a sequence pair of a given length
    seq1 = ""
    seq2 = ""
    generated = 0
    choices = ['G','A','T','C']
    while (generated < size):
        seq1 += choices[random.randint(0,3)]
        seq2 += choices[random.randint(0,3)]
        generated = generated + 1
    return(seq1+','+seq2)

def generate_sequences():
    # make sure directory exists for generated sequences
    if not os.path.exists("random_sequences"):
        os.makedirs("random_sequences")
    sizes = [500,1000,2000,4000,5000]
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
