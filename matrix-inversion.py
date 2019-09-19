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


def main(A, I):
    Am = A
    Im = I
    counter = 0

    for i in Am:
        for j in i:
            print(j)

main(A, I)
