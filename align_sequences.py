import os
import sys
import helper


def opt_align(m, n, seq1, seq2, matrix):
    # Results: 2, 2-D list/table with m rows and n columns.
    #   opt_results[i][j] = a tuple.
    #       First element  [0] = Calculated cost given length of i and j.
    #       Second element [1] = Traceback direction.
    #           Traceback list legend:
    #               0 - no traceback direction. this only occurs at the i=j=0.
    #               1 - go diaganally, i-1 & j-1. No '-' is inserted.
    #               2 - go up a row, i-1 & j. Insert a '-' on sequence 2.
    #               3 - go left a column, i & j-1. Insert a '-' on sequence 1.
    opt_results = []

    # initialize top left of table, no traceback & no cost.
    opt_results.append([(0, 0)])

    # initialize first row base cases.
    for j in range(1, n+1):
        opt_results[0].append(
            (opt_results[0][j-1][0]+helper.cost('-', seq2[j-1], matrix), 3))

    # do DP
    for i in range(1, m+1):
        # first element of j for j=0 means no length, so a '-' will always be inserted.
        # inserts a list of a tuple.
        opt_results.append(
            [(opt_results[i-1][0][0]+helper.cost(seq1[i-1], '-', matrix), 2)])

        for j in range(1, n+1):

            # set the jth value in the ith row to be the minimum of the following:
            opt_results[i].append(
                min(
                    [
                        # align i with j
                        (opt_results[i-1][j-1][0] +
                         helper.cost(seq1[i-1], seq2[j-1], matrix), 1),
                        # insert a '-' on seq2
                        (opt_results[i-1][j][0] +
                         helper.cost(seq1[i-1], '-', matrix), 2),
                        # insert a '-' on seq1
                        (opt_results[i][j-1][0] +
                         helper.cost('-', seq2[j-1], matrix), 3)
                    ],
                    # sort by the first value of the tuple, the cost
                    key=lambda tup: tup[0]
                )
            )

    # Do traceback. Gets a tuple.
    # opt_seqs[0] = opt_seq1
    # opt_seqs[1] = opt_seq2
    opt_seqs = helper.traceback_sequences(m, n, seq1, seq2, opt_results)

    # Return resulting string
    return(opt_seqs[0]+','+opt_seqs[1]+':'+str(opt_results[m][n][0]))


input_matrix = sys.argv[1]
input_sequence = sys.argv[2]

matrix = helper.parse_weight_matrix(input_matrix)
pairs = helper.parse_sequences(input_sequence)
output = open("imp2output.txt", "w")

for pair in pairs:
    seq1 = pair[0]
    seq2 = pair[1]
    m = len(seq1)
    n = len(seq2)
    output.write(opt_align(m, n, seq1, seq2, matrix) + "\n")

output.close()
