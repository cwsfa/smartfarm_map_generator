#!/usr/bin/env python3
import cv2
import numpy as np

def map_generator(filename):
    row = 0
    column = 0
    a = float(input('기둥 사이 가로 길이(m) : '))
    b = float(input('기둥 사이 세로길이(m) : '))
    c = float(input('Map resolution(px) : '))
    d = int(input('가로개수 : '))
    e = int(input('일반 기둥 점두께(px) : '))
    f = int(input('중앙통로 기둥 점두께(px) : '))
    g = float(input('중앙통로 길이(m) : '))
    h = int(input('직선 두께(px) : '))
    k = int(input('좌 공백(m) : '))
    l = int(input('우 공백(m) : '))
    m = float(input('상단하단 벽과의 (m) : '))

    # For Debug
    # a = 8
    # b = 4.5
    # c = 0.05
    # d = 5
    # e = 8
    # f = 3
    # g = 10
    # h = 5
    # k = 10
    # l = 20
    # m = 10

    horizontal_pixels = a / c
    vertical_pixels = b / c
    central_passage_pixels = g / c
    left_blank = k / c
    right_blank = l / c
    wall_station_distance = m / c

    vertical_size = int((vertical_pixels * 20) + central_passage_pixels + (wall_station_distance * 2))
    horizontal_size = int(horizontal_pixels * (d-1) + (left_blank + right_blank) * 2)

    img = np.zeros((vertical_size, horizontal_size, 3), np.uint8) + 255

    cv2.line(img, (0, int(vertical_pixels)), (horizontal_size, int(vertical_pixels)),(0,0,0), h) #가로라인 위쪽

    cv2.line(img, (int(left_blank), 0), (int(left_blank), vertical_size), (0, 0, 0), h) #세로 라인
    cv2.line(img, (int(horizontal_pixels * (d-1) + (left_blank * 2) + right_blank), 0), (int(horizontal_pixels * (d-1) + (left_blank * 2) + right_blank), vertical_size), (0, 0, 0), h)

    start_column = left_blank * 2
    column = start_column
    for i in range(0,10):
        if i == 1:
            row += wall_station_distance
        else:
            row += vertical_pixels
        for j in range(0, d):
            cv2.circle(img, (int(column), int(row)), e,(0,0,0), -1)
            column += horizontal_pixels
        column = start_column

    row += vertical_pixels
    for j in range(0, d):
        cv2.circle(img, (int(column), int(row)), f, (0, 0, 0), -1)
        column += horizontal_pixels
    column = start_column

    row += central_passage_pixels
    for j in range(0, d):
        cv2.circle(img, (int(column), int(row)), f, (0, 0, 0), -1)
        column += horizontal_pixels
    column = start_column

    for i in range(0,10):
        if i == 9:
            row += wall_station_distance
        else:
            row += vertical_pixels
        for j in range(0, d):
            cv2.circle(img, (int(column), int(row)), e, (0,0,0), -1)
            column += horizontal_pixels
        column = start_column

    cv2.line(img, (0, int(row)), (horizontal_size, int(row)), (0, 0, 0), h) #가로라인 아래쪽

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('tast.pgm', gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    filename = input("file name >> ")
    map_generator(filename)
