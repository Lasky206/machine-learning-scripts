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
    counter = 0
    focus = 0
    focus2 = 0

    for i in list(range(len(Am))):
        focus = Am[counter][counter]
        for j in list(range(len(Am[i]))):
            Am[i][j] = round(Am[i][j] / focus, 3)
            Im[i][j] = round(Im[i][j] / focus, 3)

        for j in list(range(len(Am)))[:counter] + list(range(len(Am)))[counter+1:]:
            focus2 = Am[j][counter]
            for k in list(range(len(Am[j]))):
                Am[j][k] = round(Am[j][k] - Am[counter][k] * focus2, 3)
                Im[j][k] = round(Im[j][k] - Im[counter][k] * focus2, 3)

        counter += 1

    printmatrix(Am)
    print()
    printmatrix(Im)

main(A, I)
