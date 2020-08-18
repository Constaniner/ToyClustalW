def Create_Tree_Table(Seq_Name_List):
    Tree_Table = []
    for i in Seq_Name_List:
        Tree_Table.append([i])
    return Tree_Table

def Create_Neigor_Matrix(Distance_Matrix):
    N = len(Distance_Matrix[0])
    M = [[0 for i in range(len(Distance_Matrix[0]))] for j in range(len(Distance_Matrix[0]))]
    R = [0 for i in range(len(Distance_Matrix[0]))]
    for i in range(len(Distance_Matrix[0])):
        for j in range(len(Distance_Matrix[0])):
            R[i] += round(Distance_Matrix[i][j],3)

    for i in range(len(Distance_Matrix[0])):
        for j in range(i + 1, len(Distance_Matrix[0])):
            M[i][j] = M[j][i] = round(Distance_Matrix[i][j] - (R[i] + R[j])/(N - 2) ,3)

    return [M,R]


def Find_the_smallest(Matrix):
    return_num = Matrix[0][1]
    position = [0, 1]
    for i in range(len(Matrix[0])):
        for j in range(i + 1, len(Matrix[0])):
            if (Matrix[i][j] < return_num):
                position = [i, j]
                return_num = Matrix[i][j]
    return [return_num, position]

def Create_New_DM(NODE,Distance_Matrix,R_Score,Tree_Table):
    DD = Distance_Matrix.copy()
    N = len(Distance_Matrix[0])
    positionx = NODE[1][0]
    positiony = NODE[1][1]

    Tree_Table[positionx]+= Tree_Table[positiony]
    Tree_Table.pop(positiony)

    DAB = Distance_Matrix[positionx][positiony]
    SAU = round(DAB /2 + (R_Score[positionx] - R_Score[positiony])/ (2*(N-2)),3)
    SBU = round(DAB - SAU,3)
    Tree_Table[positionx].append([SAU,SBU])

    '''
    for i in range(len(DD)):
        if i == positionx:
            DD.pop(i)
            continue
        elif i == positiony:
            DD.pop(i - 1)
            continue
        for j in range(len(DD[0])):
            if j == positionx:
                DD[i].pop(j)
            elif j == positiony:
                DD[i].pop(j-1)
            else:
                continue
    '''

    tmp = []
    for i in range(N):
        if (i == positionx) | (i == positiony):continue
        else:
            tmp.append(round((Distance_Matrix[i][positionx] + Distance_Matrix[i][positiony] - DAB)/2,3))
    DD.pop(positionx)
    DD.pop(positiony-1)
    j = 0
    for i in DD:
        i.pop(positionx)
        i.pop(positiony-1)
        i.insert(0,tmp[j])
        j+=1
    DD.insert(0,[0]+tmp)
    return DD

def NJT(Seq_Name_List,Distance_Matrix):
    N = len(Distance_Matrix[0])
    TB = Create_Tree_Table(Seq_Name_List)
    DD = Distance_Matrix.copy()
    for i in range(2,N):
        TMP = Create_Neigor_Matrix(DD)
        Nei_M = TMP[0]
        R_Score = TMP[1]
        Node = Find_the_smallest(Nei_M)
        TMP_DD = DD.copy()
        DD = Create_New_DM(Node,TMP_DD,R_Score,TB)

    U = Find_the_smallest(DD)
    U = U[0]
    SAU = round(U/(N+1),3)
    SBU = round(U-SAU,3)
    TB[-1].append([SAU,SBU])
    TTN = []
    for i in TB:
        TTN = TTN + i
    return TTN

'''
def Write_DNB(Tree_Table):
    STACK = []
    Write_Tmp = []
    position = []
    for i in Tree_Table:
        if isinstance(i,str):
            STACK.append(i)
        if (len(STACK) > 1) | (len(position)) == 0:
            Write_Tmp.append('(\n')
            Write_Tmp.append(STACK.pop(0))
            Write_Tmp.append(':')
            Write_Tmp.append(str(i[0]))
            Write_Tmp.append(',\n')
            Write_Tmp.append(STACK.pop(0))
            Write_Tmp.append(':')
            Write_Tmp.append(str(i[1]))
            Write_Tmp.append(')\n')
            position.append(len(Write_Tmp))
        elif len(STACK) == 1:
            Write_Tmp.append(str(i[0]))
            Write_Tmp.append(STACK.pop(0))
            Write_Tmp.append(str(i[1]))
        else:
            a = position.pop(0)
            Write_Tmp.insert(a-9,'(\n')
            Write_Tmp.insert(a + 1, ':')
            Write_Tmp.insert(a+2, str(i[0]))
            Write_Tmp.insert(a + 3, ',\n')
            a = position.pop(0) + 4
            Write_Tmp.insert(a, ':')
            Write_Tmp.insert(a+1, str(i[1]))
            Write_Tmp.insert(a+2, ')\n')
            for ele in range(len(position)):
                    position[ele] += 7
    print(Write_Tmp)

    DNB = open('Clustal.dnb','w')
    for i in Write_Tmp:
        DNB.write(i)
    DNB.close()
'''

def Create_Order(Tree_Table):
    Group_number = 0
    number = 0
    Order_List = []
    TMP = []
    for i in Tree_Table:
        if isinstance(i,str):
            number+=1
            TMP.append(i)
            if number > 1:
                Order_List.append(TMP)
                TMP = []
                number = 0
                Group_number += 1
        else:
            if number == 2:
                Order_List.append(TMP)
                TMP=[]
                number=0
            elif number == 1:
                TMP.append('-')
                TMP.reverse()
                Order_List.append(TMP.copy())
                TMP = []
                number = 0
            elif (number == 0) & (Group_number > 1):
                Order_List.append(['-','-'])
                Group_number -= 2
                '''else:
                TMP = [TMP[i:i+2] for i in range(0,len(TMP),2)]
                for i in TMP:
                    Order_List.append(i)
                TMP = []
                number = 0
                '''

    return Order_List

def Generate_Seq_Weights(Order_List,Tree_Table):
    Seq_Weights = {}
    TT = []
    ratio = 0
    for i in Tree_Table:
        if isinstance(i, list):
            TT.append(i)
        else:
            Seq_Weights[i] = 0
    for i in range(len(Order_List)):
        if (Order_List[i][0] == '-') & (Order_List[i][1] == '-'):
            '''
            count = 0
            for k in range(i):
                if Order_List[k][0] != '-': count += 1
                if Order_List[k][1] != '-': count += 1
            '''


            for k in range(i):
                if Order_List[k][0] != '-': Seq_Weights[Order_List[k][0]] += TT[i][0]/(ratio//2)
                if Order_List[k][1] != '-': Seq_Weights[Order_List[k][1]] += TT[i][1]/(ratio//2)

        elif (Order_List[i][0] == '-') & (Order_List[i][1] != '-'):
            ratio += 1
            for k in range(i):
                if Order_List[k][0] != '-': Seq_Weights[Order_List[k][0]] += TT[i][0]/ratio
                if Order_List[k][1] != '-': Seq_Weights[Order_List[k][1]] += TT[i][0]/ratio
            Seq_Weights[Order_List[i][1]] += TT[i][1]
        else:
            Seq_Weights[Order_List[i][0]] += TT[i][0]
            Seq_Weights[Order_List[i][1]] += TT[i][1]
            ratio += 2
    return Seq_Weights


'''
D = [[0, 0.17, 0.59, 0.59, 0.77, 0.81, 0.87], [0.17, 0, 0.6, 0.59, 0.77, 0.82, 0.86],
     [0.59, 0.60, 0, 0.13, 0.75, 0.73, 0.86], [0.59, 0.59, 0.13, 0, 0.75, 0.74, 0.88],
     [0.77, 0.77, 0.75, 0.75, 0, 0.80, 0.93], [0.81, 0.82, 0.73, 0.74, 0.8, 0, 0.9],
     [0.87, 0.86, 0.86, 0.88, 0.93, 0.90, 0]]
Seq_Name = ['A','B','C','D','E','F','G']
TB = NJT(Seq_Name,D)
print(TB)
OL = Create_Order(TB)
print(OL)
SW = Generate_Seq_Weights(OL,TB)
print(SW)


Seq_Name = ['A','B','C','D','E','F','G']
D = [[0,5,4,7,6,8],[5,0,7,10,9,11],[4,7,0,7,6,8],[7,10,7,0,5,9],[6,9,6,5,0,8],[8,11,8,9,8,0]]
TB = NJT(Seq_Name,D)
print(TB)

D = [[0, 0.2222222222222222, 0.5555555555555556, 0.5555555555555556], [0.2222222222222222, 0, 0.4444444444444444, 0.4444444444444444], [0.5555555555555556, 0.4444444444444444, 0, 0.5555555555555556], [0.5555555555555556, 0.4444444444444444, 0.5555555555555556, 0]]
Seq_Name = ['S1','S2','S3','S4']
TB = NJT(Seq_Name,D)
print(TB)
OL = Create_Order(TB)
print(OL)
Create_Draw_Length(OL,TB)
SW = Generate_Seq_Weights(OL,TB)
print(SW)

D = [[0, 0.25, 0.5, 0.375, 0.625, 0.875], [0.25, 0, 0.375, 0.375, 0.5, 0.875], [0.5, 0.375, 0, 0.25, 0.75, 0.75], [0.375, 0.375, 0.25, 0, 0.875, 0.75], [0.625, 0.5, 0.75, 0.875, 0, 0.7142857142857143], [0.875, 0.875, 0.75, 0.75, 0.7142857142857143, 0]]
Seq_Name = ['S1','S2','S3','S4','S5','s6']
TB = NJT(Seq_Name,D)
print(TB)
'''