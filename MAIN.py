import Pairwise_Alignment
import Distance_Similarity_Matrix
import Neighbor_Joining_Tree
import Plot
import Final_Part

# Read and Generate Sequence Dict
a = input('Please input file name:')
File = open(a, 'r')
Dict_Name = {}
Dict_Seq = {}
Tmp = []
status = 0
for line in File:
    if (line[0] == '>'):
        status = 1
        Tmp.append(line[1:-1])
    elif (status == 1) & (isinstance(line, str)):
        Name = Tmp.pop(0)
        Dict_Name[Name] = line[:-1]
        Dict_Seq[line[:-1]] = Name
        status = 0
    else:
        continue

Name_List = list(Dict_Name.keys())
Seq_List = list(Dict_Seq.keys())

# Do Pairwise Alignment
S_List = []
P_List = []
Similaroty_Matrix = [[1 for i in range(len(Seq_List))] for j in range(len(Seq_List))]
for i in range(len(Seq_List)):
    for j in range(i + 1, len(Seq_List)):
        seq1 = Seq_List[i]
        seq2 = Seq_List[j]
        S = [[0 for i in range(len(seq1) + 1)] for j in range(len(seq2) + 1)]
        Trace_Matrix = Pairwise_Alignment.NW_Score(seq1, seq2, S)
        PATH = Pairwise_Alignment.Get_Path(Trace_Matrix)
        Distance = Pairwise_Alignment.distance(PATH[-1], seq1)
        Similaroty_Matrix[i][j] = Similaroty_Matrix[j][i] = Distance
        Plot.Plot_PA_SM(S,Trace_Matrix,Dict_Seq[seq1],Dict_Seq[seq2],seq1,seq2)
        S_List.append(S.copy())
        P_List.append(PATH.copy())

Distance_Matrix = Distance_Similarity_Matrix.Create_Distance_Matrix(Similaroty_Matrix)
Tree_Table = Neighbor_Joining_Tree.NJT(Name_List,Distance_Matrix)
Order_List = Neighbor_Joining_Tree.Create_Order(Tree_Table)
Seq_Weight_Dict = Neighbor_Joining_Tree.Generate_Seq_Weights(Order_List,Tree_Table)
Final_Score = Final_Part.Create_S_List(S_List,Seq_Weight_Dict)
Plot.Plot_Guide_Tree(Order_List,Tree_Table)