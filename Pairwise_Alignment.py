def NW_Score(seq1, seq2,S):
    Trace_matrix = [[[] for i in range(len(seq1) + 1)] for j in range(len(seq2) + 1)]
    for i in range(len(seq1) + 1):
        S[0][i] = -2 * i
        Trace_matrix[0][i].append('GapInVer')
    for i in range(len(seq2) + 1):
        S[i][0] = -2 * i
        Trace_matrix[i][0].append('GapInHor')
    Trace_matrix[0][0] = []
    for i in range(1,len(seq2) + 1):
        for j in range(1,len(seq1) + 1):
            if (seq1[j - 1] == seq2[i - 1]):
                S[i][j] = max((S[i - 1][j - 1] + NW_match), S[i - 1][j] + NW_gap_penalty,
                              S[i][j - 1] + NW_gap_penalty)
            else:
                S[i][j] = max((S[i - 1][j - 1] + NW_mismatch), S[i - 1][j] + NW_gap_penalty,
                              S[i][j - 1] + NW_gap_penalty)

            if (S[i][j] == S[i - 1][j - 1] + NW_match) & (seq1[j - 1] == seq2[i - 1]):
                Trace_matrix[i][j].append('Match')
            if (S[i][j] == S[i - 1][j - 1] + NW_mismatch):
                Trace_matrix[i][j].append('Mismatch')
            if (S[i][j] == S[i][j - 1] + NW_gap_penalty):
                Trace_matrix[i][j].append('GapInVer')
            if (S[i][j] == S[i - 1][j] + NW_gap_penalty):
                Trace_matrix[i][j].append('GapInHor')
    '''
    for i in range(len(seq2) + 1):
            for j in range(len(seq1) + 1):
                print(S[i][j], ' ', end='')
            print('')
    '''


    return Trace_matrix

def Get_Path(Trace_matrix):
    T = [0,0]
    i = len(Trace_matrix) - 1
    j = len(Trace_matrix[0]) - 1
    T.append([i,j])
    #TODO:Compare based on Value
    while (True):
        while(True):
            if (Trace_matrix[i][j][0] == 'Match'):
                i -= 1
                j -= 1
                T.append([i,j])
                T[0] += 1
                T[1] += 1
            elif (Trace_matrix[i][j][0] == 'Mismatch'):
                i -= 1
                j -= 1
                T.append([i, j])
                T[1] -= 1
            elif (Trace_matrix[i][j][0] == 'GapInVer'):
                j -= 1
                T.append([i, j])
                T[1] -= 2
            else:
                i -= 1
                T.append([i, j])
                T[1] -= 2
            if (i == 0) | (j == 0):
                #if Trace_matrix[T[-1][0]][T[-1][1]][0] == 'Match':
                    #T[0] += 1
                T.reverse()
                return T


def distance(Match_number,seq):
    return Match_number/len(seq)





NW_gap_penalty = -2
NW_mismatch = -1
NW_match = 1
'''
seq1 = 'PYKFSIKSM'
seq2 = 'PYMYSSESM'
S = [[0 for i in range(len(seq1) + 1)] for j in range(len(seq2) + 1)]
Trace_matrix = NW_Score(seq1, seq2,S)
print(S)
for i in range(len(seq2)+1):
    print(Trace_matrix[i])
aa = Get_Path(Trace_matrix)
print(aa)
MN = aa[-1]
SS = distance(MN,seq1)
print(SS)

'''






