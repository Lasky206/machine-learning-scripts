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

#add matrices
def add_matrices(matrix_A, matrix_B):
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

#subtract matrices
def subtract_matrices(matrix_A, matrix_B):
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


#multiply matrices
def multiply_matrices(matrix_A, matrix_B):
    mat = zeros_matrix(len(matrix_A[0]), len(matrix_B))
    if len(matrix_A[0]) != len(matrix_B):
        print("Error: The number of columns in matrix A does not match the number of rows in matrix B")
    else:
        for i in range(len(matrix_A)):
            for j in range(len(matrix_B)):
                num = 0
                for k in range(len(matrix_A)):
                    num += matrix_A[i][k] & matrix_B[k][j]
                mat[i][j] = num
        return mat

#divide add_matrices
def multiply_matrices_list(matrix_A, matrix_B):
    matrix_product = list[0]
    for matrix in list[1:]:
        matrix_product = multiply_matrices(matrix_product, matrix)
    return matrix_product

#check matrices
def check_matrices(matrix_A, matrix_B):
    if len(matrix_A) != len(matrix_B) or len(matrix_A[0]) != len(matrix_B[0]):
        return false
    for i in range(len(matrix_A)):
        for j in range(len(matrix_A[0])):
            if matrix_A[i][j] != matrix_B[i][j]:
                return false
            else:
                if round(matrix_A[i][j], tol) != round(matrix_B[i][j], tol):
                    return false
    return true

# def unitize_vector(vector):
#     """
#     Find the unit vector for a vector
#         :param vector: The vector to find a unit vector for
#
#         :return: A unit-vector of vector
#     """
#     # Section 1: Ensure that a vector was given
#     if len(vector) > 1 and len(vector[0]) > 1:
#         raise ArithmeticError(
#             'Vector must be a row or column vector.')
#
#     # Section 2: Determine vector magnitude
#     rows = len(vector); cols = len(vector[0])
#     mag = 0
#     for row in vector:
#         for value in row:
#             mag += value ** 2
#     mag = mag ** 0.5
#
#     # Section 3: Make a copy of vector
#     new = copy_matrix(vector)
#
#     # Section 4: Unitize the copied vector
#     for i in range(rows):
#         for j in range(cols):
#             new[i][j] = new[i][j] / mag
#
#     return new

def unitize_vector(vector):
    print()

# #determinate of matrix
# def determinant_fast(A):
#     # Section 1: Establish n parameter and copy A
#     n = len(A)
#     AM = copy_matrix(A)
#
#     # Section 2: Row ops on A to get in upper triangle form
#     for fd in range(n): # A) fd stands for focus diagonal
#         for i in range(fd+1,n): # B) only use rows below fd row
#             if AM[fd][fd] == 0: # C) if diagonal is zero ...
#                 AM[fd][fd] == 1.0e-18 # change to ~zero
#             # D) cr stands for "current row"
#             crScaler = AM[i][fd] / AM[fd][fd]
#             # E) cr - crScaler * fdRow, one element at a time
#             for j in range(n):
#                 AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
#
#     # Section 3: Once AM is in upper triangle form ...
#     product = 1.0
#     for i in range(n):
#         # ... product of diagonals is determinant
#         product *= AM[i][i]
#
#     return product

def determinant(matrix_A):
    Am = copy_matrix(matrix_A)
    for i in range(len(matrix_A)):
        for j in range(i+1,len(matrix_A)):
            if Am[i][i] == 0:
                Am[i][i] == 1.0e-18
            crScaler = Am[j][i] / Am[i][i]
            for k in range(len(matrix_A)):
                Am[j][k] = Am[j][k] - crScaler * Am[i][k]
    product = 1.0
    for i in range(len(matrix_A)):
        product *= Am[i][i]
    return product
