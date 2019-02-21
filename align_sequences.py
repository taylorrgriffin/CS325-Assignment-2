import os
import sys
import helper

def opt_align(m,n,seq1,seq2,matrix):
    opt_results = []
    opt_results.append([(0,0)])
    for j in range(1, n+1):
        opt_results[0].append((opt_results[0][j-1][0]+helper.cost('-', seq2[j-1], matrix),3))
    for i in range(1, m+1):
        opt_results.append([(opt_results[i-1][0][0]+helper.cost(seq1[i-1], '-', matrix),2)])
        for j in range(1, n+1):
            opt_results[i].append(min(
                [
                    (opt_results[i-1][j-1][0]+helper.cost(seq1[i-1],seq2[j-1],matrix),1),
                    (opt_results[i-1][j][0]+helper.cost(seq1[i-1],'-',matrix),2),
                    (opt_results[i][j-1][0]+helper.cost('-',seq2[j-1],matrix),3)
                ]
            ,key=lambda tup: tup[0]))
    x = opt_results[m][n][1]
    i = m
    j = n
    opt_seq1 = ""
    opt_seq2 = ""
    while (x > 0):
        if (x == 1 or x == 3):
            opt_seq2 = seq2[j-1] + opt_seq2
            j = j - 1
        if (x == 1 or x == 2):
            opt_seq1 = seq1[i-1] + opt_seq1
            i = i -1
        if (x == 2):
            opt_seq2 = '-' + opt_seq2 
        if (x == 3):
            opt_seq1 = "-" + opt_seq1
        
    return(opt_seq1+','+opt_seq2+':'+opt_results[m][n][0])

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

