import os
import sys
import helper

def opt_align(m,n,seq1,seq2,matrix):
    opt_results = []
    backtrace = []
    opt_results.append([0])
    for j in range(1, n+1):
        opt_results[0].append(opt_results[0][j-1]+helper.cost('-', seq2[j-1], matrix))
    for i in range(1, m+1):
        opt_results.append([opt_results[i-1][0]+helper.cost(seq1[i-1], '-', matrix)])
        for j in range(1, n+1):
            opt_results[i].append(min(
                opt_results[i-1][j-1]+helper.cost(seq1[i-1],seq2[j-1],matrix),
                opt_results[i-1][j]+helper.cost(seq1[i-1],'-',matrix),
                opt_results[i][j-1]+helper.cost('-',seq2[j-1],matrix)
            ))
    return opt_results[m][n]

input_matrix = sys.argv[1]
input_sequence = sys.argv[2]

matrix = helper.parse_weight_matrix(input_matrix)
pairs = helper.parse_sequences(input_sequence)

for pair in pairs:
    seq1 = pair[0]
    seq2 = pair[1]
    m = len(seq1)
    n = len(seq2)
    print(opt_align(m,n,seq1,seq2,matrix))

