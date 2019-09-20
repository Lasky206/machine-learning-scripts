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

    for i, ii in zip(Am, Im):
        for j in i:
            tmpA.append(j/i[counter])
        for j in ii:
            tmpI.append(j/i[counter])
        Am[counter] = tmpA
        Im[counter] = tmpI

        print('#############################') #USED YOUR HELP FOR THIS PART HERE
        for j in list(range(len(Am)))[:counter] + list(range(len(Am)))[counter+1:]:
            #END OF HELP
            var = Am[j][counter]
            for k in Am[j]:
                print(k - var * Am[counter])



        print('#############################')

        tmpA = []
        tmpI = []
        counter += 1
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    printmatrix(Am)
    print('---------------------------------------------')
    printmatrix(Im)

main(A, I)
