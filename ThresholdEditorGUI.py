# -*- coding: utf-8 -*- 
'''
获取棋子的颜色阈值.

经过调试, 

lower = [19  0  0]
upper = [74 16 19]

'''

import cv2
import numpy as np

# 样例图片
# sample_img = cv2.imread("./samples_roi/1.png")
sample_img = cv2.imread("sucai.png",-1)
sample_img = cv2.cvtColor(sample_img,cv2.COLOR_BGR2HSV)

# 颜色阈值 Upper
threshold_upper = None
# 颜色阈值 Lower
threshold_lower = None


# 更新MASK图像，并且刷新windows
def updateMask():
    global sample_img
    global threshold_lower
    global threshold_upper

    # 计算MASK
    #sample_img = cv2.cvtColor(sample_img,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(sample_img, threshold_lower, threshold_upper)

    cv2.imshow('mask', mask)

# 更新阈值
def updateThreshold(x):

    global threshold_lower
    global threshold_upper

    minH = cv2.getTrackbarPos('minH','image')
    maxH = cv2.getTrackbarPos('maxH','image')
    minS = cv2.getTrackbarPos('minS','image')
    maxS = cv2.getTrackbarPos('maxS', 'image')
    minV = cv2.getTrackbarPos('minV', 'image')
    maxV = cv2.getTrackbarPos('maxV', 'image')
    
    threshold_lower = np.int32([minH, minS, minV])
    threshold_upper = np.int32([maxH, maxS, maxV])

    print('更新阈值')
    print(threshold_lower)
    print(threshold_upper)
    updateMask()

cv2.namedWindow('image', flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)
# cv2.namedWindow('image')
cv2.imshow('image', sample_img)

# cv2.namedWindow('mask')
cv2.namedWindow('mask', flags= cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)

# 函数原型
# createTrackbar(trackbarName, windowName, value, count, onChange) -> None
# 解释
# 在window‘iamge’ 上创建一个滑动条，起名为Channel_XXX， 设定滑动范围为0-255, 
# onChange事件回调 啥也不做

# 红色阈值 Bar
cv2.createTrackbar('minH','image',0,255,updateThreshold)
cv2.createTrackbar('maxH','image',0,255,updateThreshold)
# 绿色阈值 Bar
cv2.createTrackbar('minS','image',0,255,updateThreshold)
cv2.createTrackbar('maxS','image',0,255,updateThreshold)
# 蓝色阈值 Bar
cv2.createTrackbar('minV','image',0,255,updateThreshold)
cv2.createTrackbar('maxV','image',0,255,updateThreshold)

print("调试棋子的颜色阈值, 键盘摁e退出程序")

# 首次初始化窗口的色块
# 后面的更新 都是由getTrackbarPos产生变化而触发
updateThreshold(None)

while cv2.waitKey(0) != ord('e'):
    continue

cv2.destroyAllWindows()