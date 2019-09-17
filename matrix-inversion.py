def printmatrix(matrix):
    for line in matrix.values():
        print(line)


#matrix A
matrixA = {
'arow1':[5, 4, 3, 2, 1],
'arow2':[4, 3, 2, 1 ,5],
'arow3':[3, 2, 9, 5, 4],
'arow4':[2, 1, 5, 4, 3],
'arow5':[1, 2, 3, 4, 5]
}

#matrix I
matrixI = {
'irow1':[1, 0, 0, 0, 0],
'irow2':[0, 1, 0, 0, 0],
'irow3':[0, 0, 1, 0, 0],
'irow4':[0, 0, 0, 1, 0],
'irow5':[0, 0, 0, 0, 1]
}


#lets invert
def inversion(matrix):
    #xy axis counters
    counter = 0
    for row in list(matrix.values()):
        ph = row[counter]
        for column in row:
            print(column/ph)


inversion(matrixA)


#printmatrix(matrixA)
