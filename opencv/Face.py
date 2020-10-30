# # 1.到入库
# import  cv2
#
#
# # 2.加载图像
# img=cv2.imread("C:/Users/Kansx/Desktop/opencv/img/2.jpg")
#
# # 3.创建窗口
# cv2.namedWindow("star")
#
# # 4.显示图片
# cv2.imshow("Jameslaoshi",img)
#
# # 5.暂停窗口
# cv2.waitKey(0)
#
# # 6.关闭窗口
# cv2.destroyAllWindows()

# 1.导入库
import cv2

# 2.加载图像
img=cv2.imread("C:/Users/Kansx/Desktop/opencv/img/n.jpg")

# 3.加载人脸模型
face=cv2.CascadeClassifier("C:/Users/Kansx/Desktop/opencv/haarcascades/haarcascade_frontalface_alt.xml")

# 4.调整图片灰度，灰度可以提升性能，人脸识别没必要识别颜色
gray=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

# 5.检查人脸
faces=face.detectMultiScale(gray)

# 6.标记人脸
for (x,y,w,h) in faces:
    # 里面有四个参数，1.写图片 2.坐标原点 3.识别大小 4.颜色 5 线宽
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

# 7.创建窗口
# cv2.namedWindow("face_indentify")

# 8.显示图片
cv2.imshow("face_show",img)

# 9.暂停窗口
cv2.waitKey(0)

# 10.关闭窗口
cv2.destroyAllWindows()
