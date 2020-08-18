import Pairwise_Alignment
def Create_Similarity_Matrix(Seq_List):
    S = [[1 for i in range(len(Seq_List))] for j in range(len(Seq_List))]
    for i in range(len(Seq_List) - 1):
        for j in range(i+1,len(Seq_List)):
            seq1 = Seq_List[i]
            seq2 = Seq_List[j]
            SS = [[0 for i in range(len(seq1) + 1)] for j in range(len(seq2) + 1)]
            Trace_Matrix = Pairwise_Alignment.NW_Score(seq1,seq2,SS)
            Path = Pairwise_Alignment.Get_Path(Trace_Matrix)
            Distance = Pairwise_Alignment.distance(Path[-1],seq1)
            S[i][j] = S[j][i] = Distance
    return S

def Create_Distance_Matrix(Similarity_Matrix):
    D = [[0 for i in range(len(Similarity_Matrix[0]))] for j in range(len(Similarity_Matrix[0]))]
    for i in range(len(D[0])):
        for j in range(len(D[0])):
            D[i][j] = D[j][i] = 1 - Similarity_Matrix[i][j]
    return D

'''
Seq_List = ['PYRFTIKSM','PYKFSIKSM','PYMYSSESM','PMDDNPFSFQSM']
SM = Create_Similarity_Matrix(Seq_List)
DM = Create_Distance_Matrix(SM)
print(SM)
print(DM)

Seq_List = ['PYRFPYRF','PYRQPYRQ','PPPPPYRQ','PPPQPYRF','PYRTTFQ','PPYTRRSS']
SM = Create_Similarity_Matrix(Seq_List)
DM = Create_Distance_Matrix(SM)
print(SM)
print(DM)
'''




