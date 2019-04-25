import sys

def create_list(R):
    max_index = [0, R]
    for i in range(2,R+1):
        max_index.append(max_index[i-1] + R + i -1)
    for i in range(R+1,2*R):
        max_index.append(max_index[i-1] + 3*R - i -1)
    return max_index

def get_position(cell):
    global R
    global max_index
    for i in range(2*R-1):
        if cell <= max_index[i]:
            line = i
            if i == 0:
                seq = cell
            else:
                seq = cell - max_index[i-1]
            break
        
    return line, seq

def getCell(line, seq):
    global max_index
    return seq if line == 1 else max_index[line-1] + seq

def is_valid(line, seq):
    global R
    global back_cells
    if line < 1 or line > 2*R-1 or seq < 1 or seq > max_index[line]-max_index[line-1]:
        # print('out_of_border', str(getCell(line,seq)))
        return False
    if str(getCell(line,seq)) in bad_cells:
        # print('bad cell: ' + str(getCell(line,seq)))
        return False
    return True

def possible_move(line, seq):
    global R
    if is_valid(line,seq-1): yield (line, seq-1)
    if is_valid(line,seq+1): yield (line, seq+1)
    if line <= R:
        if is_valid(line-1, seq-1): yield (line-1, seq-1)
        if is_valid(line-1, seq): yield (line-1, seq)
    else:
        if is_valid(line-1, seq): yield (line-1, seq)
        if is_valid(line-1, seq+1): yield (line-1, seq+1)
    if line < R:
        if is_valid(line+1, seq): yield (line+1, seq)
        if is_valid(line+1, seq+1): yield (line+1, seq+1)
    else:
        if is_valid(line+1, seq-1): yield (line+1, seq-1)
        if is_valid(line+1, seq): yield (line+1, seq)
    
# Main
line1 = sys.stdin.readline()
line2 = sys.stdin.readline()

# R N A B X
paremeters=line1.split()
# Global variable
R=int(paremeters[0])
N=int(paremeters[1])
A=int(paremeters[2])
B=int(paremeters[3])
X=int(paremeters[4])
# Global variable
bad_cells=line2.split()
# print(bad_cells)
# Global variable
max_index=create_list(R)

cell_step = {A:0}
cell_stack=[A]
while len(cell_stack):
    current_cell = cell_stack.pop(len(cell_stack)-1)
    current_step = cell_step[current_cell]
    current_line, current_seq = get_position(current_cell)
    # print(current_cell, current_step, current_line, current_seq)
    for new_line, new_seq in possible_move(current_line, current_seq):
        new_cell = getCell(new_line, new_seq)
        if current_step+1 > N:
            break
        elif current_step+1 == N:
            if new_cell == B and new_cell not in cell_step.keys():
                cell_step[new_cell] = N
        elif new_cell not in cell_step.keys():
            if(new_cell != B):
                cell_stack.append(new_cell)
            cell_step[new_cell]= current_step+1
        else:    
            if current_step+1 < cell_step[new_cell]:
                if(new_cell != B):
                    cell_stack.append(new_cell)
                cell_step[new_cell]= current_step+1

if B in cell_step.keys():
    print(cell_step[B])
else:
    print('No')
