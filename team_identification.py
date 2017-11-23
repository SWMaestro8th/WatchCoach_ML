import numpy as np
import cv2
import time

# @brief : 팀을 구별해주는 함수 (메인)
# @param : 이미지
# @return : 1 (아군) ,-1 (적군), 0 (기타)
def team_division(image):
    start = time.time()


    # image load
    image_path = "/Users/itaegyeong/Desktop/testblue2.png"


    img = image # or image
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # HSV color
    boundaries = [
        ([0],[0,0,0],[1,1,1]), # 기타
        ([1],[110, 51, 51],[130, 255, 255]) # 아군
    ]

    for (code, lower, upper) in boundaries:
        lower = np.array(lower, dtype='uint8')
        upper = np.array(upper, dtype='uint8')
        mask = cv2.inRange(img_hsv, lower, upper)

        count = 0
        for i in range(0, len(mask)):
            for j in mask[i]:
                if j == 255:
                    count = count + 1

        end = time.time() - start


        if count > 10000:
            print("팀 구별 걸린시간 ", end)
            return code[0]
        else:
            print("팀 구별 걸린시간 ", end)

