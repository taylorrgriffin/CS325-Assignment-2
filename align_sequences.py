import os
import sys
import helper

def opt_align(n,m,seq1,seq2,matrix):
    return(seq1+','+seq2+':'+str(100))

input_matrix = sys.argv[1]
input_sequence = sys.argv[2]

matrix = helper.parse_weight_matrix(input_matrix)
pairs = helper.parse_sequences(input_sequence)

for pair in pairs:
    seq1 = pair[0]
    seq2 = pair[1]
    n = len(seq1)
    m = len(seq2)
    print(opt_align(n,m,seq1,seq2,matrix))

