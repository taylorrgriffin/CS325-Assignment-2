#!/usr/bin/python
import os
import csv

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
