import xlsxwriter
import turtle
import os

def Plot_PA_SM(Align_Matrix,Trace_Matrix,seq1_name,seq2_name,seq1,seq2):
    if not os.path.exists(os.getcwd()+'/Excel'):os.mkdir(os.getcwd()+'/Excel')
    TT = Trace_Matrix.copy()
    workbook = xlsxwriter.Workbook(os.getcwd()+'/Excel/'+seq1_name+'&'+seq2_name+'.xlsx')
    worksheet = workbook.add_worksheet(seq1_name+'&'+seq2_name)
    Style = workbook.add_format({
        'bold': True,
        'fg_color': 'yellow',
    })
    for i in range(len(seq1)):
        worksheet.write(0, i+2, seq1[i])
    for i in range(len(seq2)):
        worksheet.write(i+2, 0, seq2[i])
    for i in range(len(Align_Matrix)):
        for j in range(len(Align_Matrix[0])):
            if (i == TT[0][0]) & (j == TT[0][1]):
                worksheet.write(i + 1, j + 1, Align_Matrix[i][j],Style)
                TT.pop(0)
            else :
                worksheet.write(i+1,j+1,Align_Matrix[i][j])
    workbook.close()

def Plot_Guide_Tree(Order_List,Tree_Table):
    '''
    turtle.hideturtle()
    turtle.setup(width=0.6, height=0.6)
    turtle.penup()
    turtle.goto(100,100)
    turtle.pendown()
    turtle.setheading(180)
    TT = Tree_Table.copy()
    Tmp = []
    position = [[100,100]]
    for i in Tree_Table:
        if isinstance(i,str):
            Tmp.append(i)
        else:
            position.append([position[-1][0]- 10*i[0],position[-1][1]])
            position.append([position[-1][0],position[-1][1] - 5])
    '''
    turtle.setup(width=0.6, height=0.8)
    turtle.penup()
    turtle.speed('slowest')


    TT = []
    position = [(100,100)]
    for i in Tree_Table:
        if isinstance(i, list):
            TT.append(i)


    for i in range(len(Order_List)):
        if (Order_List[i][0] == '-') & (Order_List[i][1] == '-'):
            pos1 = position.pop(1)
            pos2 = position.pop(1)
            turtle.goto(pos1[0],pos1[1])
            turtle.setheading(180)

            turtle.pendown()
            turtle.forward(100 * TT[i][0])
            pos = turtle.pos()
            turtle.lt(90)
            turtle.goto(pos[0],(pos2[1] + pos1[1])/2)
            pos = turtle.pos()
            position.append(pos)
            turtle.goto(pos[0], pos2[1])
            turtle.lt(90)
            turtle.goto(pos2[0], pos2[1])
            turtle.penup()

        elif (Order_List[i][0] == '-') & (Order_List[i][1] != '-'):
            pos = position.pop(-1)
            turtle.goto(pos[0],pos[1])
            turtle.setheading(180)

            turtle.pendown()
            turtle.forward(500 * TT[i][0])
            pos_tmp = turtle.pos()
            turtle.lt(90)
            turtle.goto(pos_tmp[0],position[0][1])
            pos = turtle.pos()
            position.append(pos)
            turtle.goto(pos[0],2*position[0][1] - pos_tmp[1])
            turtle.lt(90)
            pos = turtle.pos()
            turtle.goto(100,pos[1])
            position[0] = turtle.pos()
            #turtle.setx(110)
            turtle.write(Order_List[i][1], False, align="left")
            turtle.penup()
        else:
            turtle.goto(100,position[0][1])
            turtle.setheading(180)
            turtle.sety(position[0][1] - 50)

            turtle.pendown()
            turtle.write(Order_List[i][0],False,align = "left")
            turtle.forward(100*TT[i][0])
            turtle.lt(90)
            turtle.forward(50*(TT[i][0] + TT[i][1]))
            pos = turtle.pos()
            position.append(pos)
            turtle.forward(50 * (TT[i][0] + TT[i][1]))
            turtle.lt(90)
            turtle.forward(100 * TT[i][1])
            turtle.write(Order_List[i][1], False, align="left")
            position[0] = turtle.pos()
            turtle.penup()

    ts = turtle.getscreen()
    ts.getcanvas().postscript(file=("Guide_Tree.eps"))
    turtle.done()


'''
TB = ['A', 'B', [0.084, 0.086], 'C', 'D', [0.062, 0.068], [0.216, 0.227], 'E', [0.062, 0.402], 'F', [0.013, 0.394], 'G', [0.063, 0.443]]
OL = [['A', 'B'], ['C', 'D'], ['-', '-'], ['-', 'E'], ['-', 'F'], ['-', 'G']]
Plot_Guide_Tree(OL,TB)


seq1_name = 'PYK'
seq2_name = 'PYM'
seq1 = 'PYKFSIKSM'
seq2 = 'PYMYSSESM'
AA = [[0, -2, -4, -6, -8, -10, -12, -14, -16, -18], [-2, 1, -1, -3, -5, -7, -9, -11, -13, -15], [-4, -1, 2, 0, -2, -4, -6, -8, -10, -12], [-6, -3, 0, 1, -1, -3, -5, -7, -9, -9], [-8, -5, -2, -1, 0, -2, -4, -6, -8, -10], [-10, -7, -4, -3, -2, 1, -1, -3, -5, -7], [-12, -9, -6, -5, -4, -1, 0, -2, -2, -4], [-14, -11, -8, -7, -6, -3, -2, -1, -3, -3], [-16, -13, -10, -9, -8, -5, -4, -3, 0, -2], [-18, -15, -12, -11, -10, -7, -6, -5, -2, 1]]
TM = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], 1, 5]
Plot_PA_SM(AA,TM,seq1_name,seq2_name,seq1,seq2)
'''
