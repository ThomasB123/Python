

def validNeighbours(x,y):
    neighbours = []
    if x < 3:
        neighbours.append([x+1,y])
        if y < 3:
            neighbours.append([x+1,y+1])
        if y > 0:
            neighbours.append([x+1,y-1])        
    if x > 0:
        neighbours.append([x-1,y])
        if y < 3:
            neighbours.append([x-1,y+1])
        if y > 0:
            neighbours.append([x-1,y-1])        
    if y < 3:
        neighbours.append([x,y+1])
    if y > 0:
        neighbours.append([x,y-1])
    return(neighbours)

print(validNeighbours(0,0))

