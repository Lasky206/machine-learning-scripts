def printmatrix(matrix):
    for line in matrix.values():
        print(line)


#matrix A
A = [
[5, 4, 3, 2, 1],
[4, 3, 2, 1 ,5],
[3, 2, 9, 5, 4],
[2, 1, 5, 4, 3],
[1, 2, 3, 4, 5]
]

#matrix I
I = [
[1, 0, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 1]
]


# #lets invert
# def inversion(matrix):
#     #morphing matracies
#     Am = []
#     Im = []
#     #xy axis counters
#     counter = 0
#     for row in matrix:
#         focus = row[counter]
#         rowph = []
#         sub = []
#         for column in row:
#             rowph.append(column/focus)
#             sub.append(column*3)
#         Am.append(rowph)
#     for row in Am:
#         print(row)
#     for row in Im:
#         print(row)
#
#
# inversion(A)


#printmatrix(matrixA)

def inversion(matrix):
    counter = 0
    Am = matrix
    Im = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
    ]
    for i in range(len(A)):
        tmpA = []
        tmpI = []
        row = A[counter]
        column = row[counter]
        for num in A[0]:
            tmpA.append(num/column)
        for num in I[0]:
            tmpI.append(num/column)
        for num in range(len(tmpA)):
            tmpA*3


inversion(A)
