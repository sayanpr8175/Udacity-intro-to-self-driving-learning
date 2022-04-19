import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    
    for i in range(len(beliefs)):
        
        #print len(beliefs[i])
        new_belief_sub = []
        for j in range(len(beliefs[i])):
            
            #print beliefs[i][j]
            if(grid[i][j]==color):
                new_belief_sub.append(beliefs[i][j]*p_hit)
            else:
                new_belief_sub.append(beliefs[i][j]*p_miss)
                
        new_beliefs.append(new_belief_sub)
    
    new_sum = 0.0
    for i in range(len(new_beliefs)):
        new_sum = new_sum+sum(new_beliefs[i])
    
    for i in range(len(new_beliefs)):
        for j in range(len(new_beliefs[i])):
            
            new_beliefs[i][j] = float(new_beliefs[i][j])/ float(new_sum)  
        
    #
    # TODO - implement this in part 2
    #

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            #pdb.set_trace()
            #print(new_i)
            #print(new_j)
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)