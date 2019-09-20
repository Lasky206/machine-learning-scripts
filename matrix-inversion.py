def printmatrix(matrix):
    for line in matrix:
        print(line)


# #matrix A
# A = [
# [5, 4, 3, 2, 1],
# [4, 3, 2, 1 ,5],
# [3, 2, 9, 5, 4],
# [2, 1, 5, 4, 3],
# [1, 2, 3, 4, 5]
# ]
#
# #matrix I
# I = [
# [1, 0, 0, 0, 0],
# [0, 1, 0, 0, 0],
# [0, 0, 1, 0, 0],
# [0, 0, 0, 1, 0],
# [0, 0, 0, 0, 1]
# ]

#matirx A
A = [
[5, 3, 1],
[3, 9, 4],
[1, 3, 5]
]

#matrix I
I = [
[1, 0, 0],
[0, 1, 0],
[0, 0, 1]
]


def main(A, I):
    Am = A
    Im = I
    tmpA = []
    tmpI = []
    counter = 0
    iterate = 0

    for i in list(range(len(Am)))[:counter] + list(range(len(Am)))[counter+1:]:
        print(Am[i][counter])


main(A, I)
