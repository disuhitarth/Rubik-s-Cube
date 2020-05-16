import numpy as np

x = np.arange(108)
# x
x = x.reshape(9, 12)
##print(x)
##print(x[0])
##print(np.size(x, 0))
for i in range(0, np.size(x, 0)):
    x[i] = 0
##print(x)

# Yellow
x[0][3], x[0][4], x[0][5] = 1, 1, 1
x[1][3], x[1][4], x[1][5] = 1, 1, 1
x[2][3], x[2][4], x[2][5] = 1, 1, 1
##OTHER
x[3][0], x[3][1], x[3][2] = 2, 2, 2
x[4][0], x[4][1], x[4][2] = 2, 2, 2
x[5][0], x[5][1], x[5][2] = 2, 2, 2

x[3][3], x[3][4], x[3][5] = 3, 3, 3
x[4][3], x[4][4], x[4][5] = 3, 3, 3
x[5][3], x[5][4], x[5][5] = 3, 3, 3

x[3][6], x[3][7], x[3][8] = 4, 4, 4
x[4][6], x[4][7], x[4][8] = 4, 4, 4
x[5][6], x[5][7], x[5][8] = 4, 4, 4

x[3][9], x[3][10], x[3][11] = 5, 5, 5
x[4][9], x[4][10], x[4][11] = 5, 5, 5
x[5][9], x[5][10], x[5][11] = 5, 5, 5

# BOTTOM

x[6][3], x[6][4], x[6][5] = 6, 6, 6
x[7][3], x[7][4], x[7][5] = 6, 6, 6
x[8][3], x[8][4], x[8][5] = 6, 6, 6

# print(x)
x_final = x


def right():
    temp1 = x[3][5]
    temp2 = x[4][5]
    temp3 = x[5][5]
    print(temp1, temp2, temp3)
    x[3][5], x[4][5], x[5][5] = x[6][5], x[7][5], x[8][5]
    x[6][5], x[7][5], x[8][5] = x[5][9], x[4][9], x[3][9]
    x[5][9], x[4][9], x[3][9] = x[0][5], x[1][5], x[2][5]
    x[0][5], x[1][5], x[2][5] = temp1, temp2, temp3  # x[3][5], x[4][5], x[6][5]

    temp4, temp5, temp6, temp7, temp8, temp9 = x[3][6], x[3][7], x[3][8], x[4][8], x[5][8], x[5][7]
    x[3][8], x[4][8], x[5][8] = x[3][6], x[3][7], x[3][8]
    x[3][7], x[4][7], x[5][7] = x[4][6], x[4][7], temp7  # x[4][8]
    x[3][6], x[4][6], x[5][6] = x[5][6], temp9, temp8  # x[5][7],x[5][8]
    print("Right happened")
    # print(x[3][5], x[4][5], x[5][5])


def right_dash():
    temp1 = x[3][5]
    temp2 = x[4][5]
    temp3 = x[5][5]
    print(temp1, temp2, temp3)
    x[3][5], x[4][5], x[5][5] = x[0][5], x[1][5], x[2][5]  # x[6][5], x[7][5], x[8][5]
    x[0][5], x[1][5], x[2][5] = x[5][9], x[4][9], x[3][9]
    x[5][9], x[4][9], x[3][9] = x[6][5], x[7][5], x[8][5]  # x[0][5], x[1][5], x[2][5]
    x[6][5], x[7][5], x[8][5] = temp1, temp2, temp3  # x[3][5], x[4][5], x[6][5]

    temp4, temp5, temp6, temp7, temp8, temp9 = x[3][6], x[3][7], x[3][8], x[4][6], x[5][6], x[5][7]
    x[3][6], x[4][6], x[5][6] = temp6, temp5, temp4
    x[3][7], x[4][7], x[5][7] = x[4][8], x[4][7], temp7  # x[4][8]
    x[3][8], x[4][8], x[5][8] = x[5][8], temp9, temp8  # x[5][7],x[5][8]
    print("Right dash happened")
    # print(x[3][5], x[4][5], x[5][5])


right()
right_dash()
print(x)