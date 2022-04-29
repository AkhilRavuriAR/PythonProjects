from collections import defaultdict


def assignvaluetoanode(node):
    val = (node.prob).pop()
    node.value =val 
    node.prob = set()
    global count
    count+=1
    current_row = row[node.index[0]]
    for kal in current_row:
        kal.prob = kal.prob-{node.value}
        if len(kal.prob) ==1:
            assignvaluetoanode(kal)
    current_col = col[node.index[1]]  
    for kal in current_col:
        kal.prob = kal.prob-{node.value}
        if len(kal.prob) ==1:
            assignvaluetoanode(kal)
    current_box = boxes[node.index[2]]
    for kal in current_box:
        kal.prob = kal.prob-{node.value}
        if len(kal.prob) ==1:
            assignvaluetoanode(kal)
            


def keepelementsintosudoku(A):
    global count
    count = 0
    for i in range(9):
        for j in range(9):
            if len(A[i][j].prob)==1:
                assignvaluetoanode(A[i][j])
    for i in range(1,10):
        for current_box in boxes:
            row_set = set()
            col_set = set()
            for slot in current_box:
                if i in slot.prob:
                    row_set.add(slot.index[0])
                    col_set.add(slot.index[1])
            if len(row_set)==1:
                current_row = row[row_set.pop()]
                for el in current_row:
                    if boxes[el.index[2]]!=current_box:
                        el.prob = el.prob-{i}
                        if len(el.prob) ==1:
                            assignvaluetoanode(el)
            if len(col_set)==1:
                current_col = col[col_set.pop()]
                for el in current_col:
                    if boxes[el.index[2]]!=current_box:
                        el.prob = el.prob-{i}
                        if len(el.prob) ==1:
                            assignvaluetoanode(el)     
        for current_row in row:
            number = 0
            for slot in current_row:
                if i in slot.prob:
                    number+=1
                    node = slot
            if number==1:
                node.prob = {i}
                assignvaluetoanode(node)
                
        for current_col in col:
            number = 0
            for slot in current_col:
                if i in slot.prob:
                    number+=1
                    node = slot
            if number==1:
                node.prob = {i}
                assignvaluetoanode(node)            
    
    return count
    

row = [row1,row2,row3,row4,row5,row6,row7,row8,row9] = [[],[],[],[],[],[],[],[],[]]
col = [col1,col2,col3,col4,col5,col6,col7,col8,col9] = [[],[],[],[],[],[],[],[],[]]


class Node:
    def __init__(self,value):
        self.value = value
        self.prob = {1,2,3,4,5,6,7,8,9}
        self.index = None

A = []
for i in range(9):
    B = list(map(int, input().split()))
    for j in range(9):
        temp = Node(B[j])
        if i<3 and j<3:
            box = 0
        elif i<3 and 3<=j<6:
            box = 1
        elif i<3 and 6<=j<9:
            box = 2
        elif 3<=i<6 and j<3:
            box = 3
        elif 3<=i<6 and 3<=j<6:
            box = 4
        elif 3<=i<6 and 6<=j<9:
            box = 5
        elif 6<=i<9 and j<3:
            box = 6
        elif 6<=i<9 and 3<=j<6:
            box = 7
        elif 6<=i<9 and 6<=j<9:
            box = 8   
        temp.index = [i,j,box]
        if B[j]!=0:
            temp.prob = set()
        B[j]=temp   
        if i==0:
            row1.append(B[j])
        elif i==1:
            row2.append(B[j])
        elif i==2:
            row3.append(B[j])
        elif i==3:
            row4.append(B[j])
        elif i==4:
            row5.append(B[j])
        elif i==5:
            row6.append(B[j])
        elif i==6:
            row7.append(B[j])
        elif i==7:
            row8.append(B[j])
        elif i==8:
            row9.append(B[j])    
        if j ==0:
            col1.append(B[j])
        elif j==1:
            col2.append(B[j])
        elif j==2:
            col3.append(B[j])
        elif j==3:
            col4.append(B[j]) 
        elif j==4:
            col5.append(B[j])
        elif j==5:
            col6.append(B[j])    
        elif j==6:
            col7.append(B[j])   
        elif j==7:
            col8.append(B[j]) 
        elif j==8:
            col9.append(B[j])    
    A.append(B)
box1 = row1[0:3]+row2[0:3]+row3[0:3]
box2 = row1[3:6]+row2[3:6]+row3[3:6]
box3 = row1[6:9]+row2[6:9]+row3[6:9]
box4 = row4[0:3]+row5[0:3]+row6[0:3]
box5 = row4[3:6]+row5[3:6]+row6[3:6]
box6 = row4[6:9]+row5[6:9]+row6[6:9]
box7 = row7[0:3]+row8[0:3]+row9[0:3]
box8 = row7[3:6]+row8[3:6]+row9[3:6]
box9 = row7[6:9]+row8[6:9]+row9[6:9]    

boxes = [box1,box2,box3,box4,box5,box6,box7,box8,box9]

for i in range(9):
    for j in range(9):
        if A[i][j].value!=0:
            current_row = row[A[i][j].index[0]]
            for val in current_row:
                val.prob = val.prob-{A[i][j].value}
            current_col = col[A[i][j].index[1]]  
            for val in current_col:
                val.prob = val.prob-{A[i][j].value}
            current_box = boxes[A[i][j].index[2]]
            for val in current_box:
                val.prob = val.prob-{A[i][j].value}



count_count = 0
while True:
    count = keepelementsintosudoku(A)
    if count==0:
        count_count+=1
    if count_count==2:
        break
dic = defaultdict(int)
for i in range(9):
        for j in range(8):
            print(A[i][j].value,end = " ")
        print(A[i][j+1].value)
for i in range(9):
    Sum = 0
    for j in range(9):
        dic[A[i][j].value] +=1
        
if max(list(dic.values()))>9:
    print("Please provide a valid sudoku with only 1 solution")
elif max(list(dic.values()))==9 and min(list(dic.values())) !=9:
    print("Given number of inputs is not sufficient to solve the sudoku")
elif max(list(dic.values()))<9:
    print("Given number of inputs is not sufficient to solve the sudoku")
else:    
    for i in range(9):
        for j in range(8):
            print(A[i][j].value,end = " ")
        print(A[i][j+1].value)