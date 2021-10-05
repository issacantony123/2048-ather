import numpy as np
import random
import os

def fill_random(mat):       #fill the given matrix with 2 or 4 randomly in empty cells(cells with 0)
    zero_places = []        #record the cells with 0
    two_or_four = [2,4]
    two_or_four_index = random.randint(0,1) #select what to fill randomly
    flag = False
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                flag = True #if at least one cell is empty
                temp = []
                temp.append(i)
                temp.append(j)
                zero_places.append(temp)

    if flag == False: #no cell is empty
        return False, mat            
    length = len(zero_places)
    n = random.randint(0,length-1)  #select a random 0 cell
    
    mat[zero_places[n][0]][zero_places[n][1]] = two_or_four[two_or_four_index] #fill the selected cell with 2 or 4
    # two_or_four[random.randint(0,2)]
    
    return True, mat


def print_matrix(mat):  #for printing mat in a formatted way
    s = [[str(e) for e in row] for row in mat]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n\n'.join(table))

def process_row(r):     #process a row 
    temp_r = [0]*4
    final_r = [0]*4
    won = False
    i = 0
    # flag = 0
    for c in r:         #for shrinking the values in the row initially
        if c!=0:
            temp_r[i] = c
            i+=1

    for c in range(3):
        if temp_r[c+1]==temp_r[c]: # add the values if 2 adjacent cells are of equal value
            temp_r[c+1] = 0   #fill the next cell with 0 and
            temp_r[c] *= 2  #fill that value with twice the value
    
    i=0
    for c in temp_r:
        if c == 2048: # check simultaneously each cell if it is 2048
            won = True

        if c!=0:
            final_r[i] = c  #for shrinking the row once again
            i+=1
    return won ,final_r     # return the won flag along with the final row

def left(x):        #processing a direction
    win_flag = False         #processing a direction
    for row in range(4): # process each row with and take up the won status
        win, temp = process_row(x[row])
        if win:
            win_flag = True
        x[row] = temp
    return win_flag, x #return win status and the processed matrix


# arr = [[0]*4]*4
arr = [[1024,1024,8,16],[16,8,4,2],[2,4,8,16],[16,8,4,2]]
# arr = [[2,0,4,4],[0,0,0,0],[0,0,4,0],[2,0,4,0]]
nump_arr = np.array(arr) #made it numpy for using transpose

f, nump_arr = fill_random(nump_arr) #fill two random values initially
f, nump_arr = fill_random(nump_arr)
flag = True

while(flag): 
    print_matrix(nump_arr) # print the matrix
    dir = int(input()) # input direction
    print("\n")
#     clear = lambda: os. system('cls') 
#     clear() # can be commented to see the matrix flow
#     print("\n")

    if(dir == 1):
        w, nump_arr_result = left(nump_arr) #call left function and take the win status
        
    if(dir == 3):
        w, nump_arr_temp = left(np.transpose(nump_arr)) #transpose the matrix and call left() for performing up direction
        nump_arr_result = np.transpose(nump_arr_temp)

    if(dir == 2):
        nump_arr_result = np.flip(nump_arr,1) #flip the matrix
        w, nump_arr_result = left(nump_arr_result)  # perform normal left transformation
        nump_arr_result = np.flip(nump_arr_result,1) # flip it again to get right transformation

    if(dir == 4):
        nump_arr_result = np.flip(nump_arr,0)  #flip vertically
        w, nump_arr_temp = left(np.transpose(nump_arr_result)) #tanspose array and apply left()
        nump_arr_result = np.transpose(nump_arr_temp)   #again take transpose
        nump_arr_result = np.flip(nump_arr_result,0) #again flip to get the final down transformation

    # print(w)
    if(w == True):
        print("You Won") # if returned win status is true
        break

    flag, nump_arr = fill_random(nump_arr_result) #fill the empty slot
    if(flag == False): #if not place to fill 2 or 4 then game over
        print("Game Over")
        break

# print_matrix(nump_arr)



            
