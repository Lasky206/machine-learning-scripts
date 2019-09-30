A = [
[5, 4, 3, 2, 1],
[4, 3, 2, 1 ,5],
[3, 2, 9, 5, 4],
[2, 1, 5, 4, 3],
[1, 2, 3, 4, 5]
]

#print matrix
def print_matrix(matrix):
    for i in matrix:
        print(i)

#zeros matrix
def zeros_matrix(rows, columns):
    mat = []
    for i in list(range(rows)):
        mat.append([])
        for j in list(range(columns)):
            mat[i].append(0)
    return mat

#identity matrix
def identity_matrix(rows, columns):
    counter = 0
    mat = []
    for i in list(range(rows)):
        mat.append([])
        for j in list(range(columns)):
            mat[i].append(0)
    for i in list(range(len(mat))):
        for j in list(range(len(mat[i]))):
            mat[counter][counter] = 1
        counter += 1
    return mat

#copy matrix
def copy_matrix(matrix):
    mat = []
    for i in list(range(len(matrix))):
        mat.append([])
        for j in list(range(len(matrix[i]))):
            mat[i].append(0)
    for i in list(range(len(matrix))):
        for j in list(range(len(mat[i]))):
            mat[i][j] = matrix[i][j]
    return mat

#transpose matrix
def copy_matrix(matrix):
    mat = []
    for i in list(range(len(matrix))):
        mat.append([])
        for j in list(range(len(matrix[i]))):
            mat[i].append(0)
    for i in list(range(len(matrix))):
        for j in list(range(len(mat[i]))):
            mat[i][j] = matrix[j][i]
    return mat

#add matricies
def add_matricies(matrix_A, matrix_B):
    mat = []
    if len(matrix_A) != len(matrix_B):
        print("Error: The number of rows does not match")
    elif len(matrix_A[0]) != len(matrix_B[0]):
        print("Error: The number of columns does not match")
    else:
        for i in list(range(len(matrix_A))):
            mat.append([])
            for j in list(range(len(matrix_A[i]))):
                mat[i].append(matrix_A[i][j]+matrix_B[i][j])
    return mat

#subtract matricies
def subtract_matricies(matrix_A, matrix_B):
    mat = []
    if len(matrix_A) != len(matrix_B):
        print("Error: The number of rows does not match")
    elif len(matrix_A[0]) != len(matrix_B[0]):
        print("Error: The number of columns does not match")
    else:
        for i in list(range(len(matrix_A))):
            mat.append([])
            for j in list(range(len(matrix_A[i]))):
                mat[i].append(matrix_A[i][j] - matrix_B[i][j])
    return mat

print_matrix(subtract_matricies(A, identity_matrix(5,5)))
