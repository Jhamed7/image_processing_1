import cv2
import numpy as np


def show_pic(img):
    cv2.imshow('pic', img)
    cv2.waitKey()


def complement(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = 255 - img[i, j]
    return img


# ----------------------- Number 1 -------------------

chess_board = np.zeros([640, 640], dtype=np.uint8)

for i in range(chess_board.shape[0]):
    for j in range(chess_board.shape[1]):
        if (i // 80) % 2 == 1:
            if (j // 80) % 2 == 0:
                chess_board[i, j] = 255
        else:
            if (j // 80) % 2 == 1:
                chess_board[i, j] = 255

# show_pic(chess_board)

# ----------------------- Number 2 -------------------

image1 = cv2.imread(r'21\1.jpg')
image2 = cv2.imread(r'21\2.jpg')

# show_pic(complement(image1))
# show_pic(complement(image2))

# ----------------------- Number 3 -------------------

image3 = cv2.imread(r'21\3.jpg')
image3 = cv2.cvtColor(image3, cv2.COLOR_RGB2GRAY)

h = image3.shape[0]
w = image3.shape[1]
new_img = np.zeros([h, w], dtype=np.uint8)

for i in range(h):
    for j in range(w):
        new_img[i, j] = image3[h-1-i, w-1-j]

# show_pic(new_img)

# ----------------------- Number 4 -------------------

image4 = cv2.imread(r'21\4.jpg')
image4 = cv2.cvtColor(image4, cv2.COLOR_RGB2GRAY)

tresh = 50

h = image4.shape[0]
w = image4.shape[1]
image5 = np.zeros([h, w], dtype=np.uint8)

for i in range(h):
    for j in range(w):
        if image4[i, j] > tresh:
            image5[i, j] = 255
        else:
            image5[i, j] = image4[i, j]

# show_pic(image5)
