#!/usr/bin/env python3
import cv2
import numpy as np

def map_generator(filename):
    row = 0
    column = 0

    a = float(input('a- 기둥 사이 가로 길이(m) : '))
    b = float(input('b- 기둥 사이 세로길이(m) : '))
    c = float(input('c- Map resolution(px) : '))
    d = int(input('d- 가로개수 : '))
    e = int(input('e- 일반 기둥 점두께(px) : '))
    f = int(input('f- 중앙통로 기둥 점두께(px) : '))
    g = float(input('g- 중앙통로 길이(m) : '))
    h = int(input('h- 직선 두께(px) : '))
    k = int(input('k- 좌 공백(m) : '))
    l = int(input('l- 우 공백(m) : '))
    m = float(input('m- 상단하단 벽과의 (m) : '))
    q = float(input('q - 배지 시작 위치(m) : '))
    r = float(input('r - 기둥과 배지 사이 거리(m) : '))
    o = float(input('o - 배지 사이 거리(m) : '))
    p = float(input('p - 중앙통로 기둥과 배지 사이 거리(m) : '))
    s = float(input('s - 배지 두께(m) : '))

    
  
    # # For Debug
    # a = 8.6 # 기둥 사이 가로 길이(m)
    # b = 4.5 # 기둥 사이 세로 길이
    # c = 0.05 # map resolution
    # d = 24 # 가로 개수 
    # e = 8 # 일반 기둥 점 두께(px)
    # f = 3 # 중앙통로 기둥 점 두께
    # g = 10 # 중앙 통로 길이
    # h = 5 # 직선 두께
    # k = 10 # 좌 공백
    # l = 10 # 우 공백
    # m = 10 # 상단하단 벽과의 거리 


    # q = 5 # 배지 시작위치 
    # r = 1.5  # 기둥과 배지 사이 거리 
    # o = 1.5  # 배지사이거리 
    # p = 0.3 # 중앙통로 기둥과 배지 사이 거리
    # s = 0.25  # 배지두께


    horizontal_pixels = a / c
    vertical_pixels = b / c
    central_passage_pixels = g / c
    left_blank = k / c
    right_blank = l / c
    wall_station_distance = m / c

    
    crops_wall_distance = q / c
    crops_distance = r / c
    crops_between_distance = o / c
    crops_between_central_distance = p / c
    crops = s / c
    
    vertical_size = int((vertical_pixels * 20) + central_passage_pixels + (wall_station_distance * 2))
    horizontal_size = int(horizontal_pixels * (d-1) + (left_blank + right_blank) * 2)
    top_crops_vertical_size = int((vertical_pixels * 10) - crops_between_central_distance + central_passage_pixels )
    bottom_crops_vertical_size2 = int((vertical_pixels * 19) + central_passage_pixels + wall_station_distance * 2 ) - int(crops_wall_distance)

    img = np.zeros((vertical_size, horizontal_size, 3), np.uint8) + 255

    cv2.line(img, (0, int(vertical_pixels)), (horizontal_size, int(vertical_pixels)),(0,0,0), h) #가로라인 위쪽

    cv2.line(img, (int(left_blank), 0), (int(left_blank), vertical_size), (0, 0, 0), h) #세로 라인
    cv2.line(img, (int(horizontal_pixels * (d-1) + (left_blank * 2) + right_blank), 0), (int(horizontal_pixels * (d-1) + (left_blank * 2) + right_blank), vertical_size), (0, 0, 0), h)
#----------------------------------------------------상단------------------------------------------------------------------------------------------------------------------
    start_column = left_blank * 2
    column = start_column
    for i in range(0,10):
        if i == 1:
            row += wall_station_distance
        else:
            row += vertical_pixels
        for j in range(0, d):
            cv2.circle(img, (int(column), int(row)), e,(0,0,0), -1)
            if i == 1:
                top_start_x = column + crops_distance
                for z in range(0,5):
                    cv2.line(img, (int(top_start_x), int(vertical_pixels + crops_wall_distance)), (int(top_start_x), top_crops_vertical_size), (255,75,34), int(crops))
                    top_start_x += crops_between_distance
            column += horizontal_pixels
        column = start_column
#----------------------------------------------------상단 통로 기둥------------------------------------------------------------------------------------------------------------------

    row += vertical_pixels
    for j in range(0, d):
        cv2.circle(img, (int(column), int(row)), f, (0, 0, 0), -1)
        column += horizontal_pixels
    column = start_column
#----------------------------------------------------하단 통로 기둥------------------------------------------------------------------------------------------------------------------

    row += central_passage_pixels
    for j in range(0, d):
        cv2.circle(img, (int(column), int(row)), f, (0, 0, 0), -1)
        bottom_start_x = column + crops_distance
        for z in range(0,5):
            cv2.line(img, (int(bottom_start_x), int(row + crops_between_central_distance)), (int(bottom_start_x), int(bottom_crops_vertical_size2)), (255,75,34), int(crops))
            bottom_start_x += + crops_between_distance
        column += horizontal_pixels
    column = start_column
#----------------------------------------------------하단------------------------------------------------------------------------------------------------------------------

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
    cv2.imwrite(filename + '.pgm', gray)
    print(filename + ".pgm is saved.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    filename = input("file name >> ")
    map_generator(filename)
