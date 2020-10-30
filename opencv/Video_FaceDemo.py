# 调用摄像头

# 思路：
# 1.导入库.
import cv2

# 加载人脸模型
face=cv2.CascadeClassifier("C:/Users/Kansx/Desktop/opencv/haarcascades/haarcascade_frontalface_alt.xml")
# 2.打开摄像头.
# VideoCapture()中参数是0，表示打开笔记本的内置摄像头
capture=cv2.VideoCapture(0)

# 3.获取摄像头实时画面

#cv2.namedWindow("camera")
# 返回true表示成功，false表示不成功
while capture.isOpened():
    # 3.1 读取摄像头的帧画面
    # cap.read()按帧读取视频，ret,frame是获cap.read()方法的两个返回值。其中ret是布尔值
    # ，如果读取帧是正确的则返回True，如果文件读取到结尾，
    # 它的返回值就为False。frame就是每一帧的图像，是个三维矩阵
    ret,frame=capture.read()
    # 图片灰度调整
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    #检查人脸
    faces=face.detectMultiScale(gray,1.1,3,0,(100,100))
    # 标记人脸
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    # 3.2 显示图片(渲染图片)
        cv2.imshow("ksx",frame)
        # 3.3 暂停窗口
        # 参数是1，表示延时1ms切换到下一帧图像，参数过大如cv2.waitKey(1000)，会因为延时过久而卡顿感觉到卡顿。
        # 参数为0，如cv2.waitKey(0)只显示当前帧图像，相当于视频暂停。
        c=cv2.waitKey(1)
        if c==27:
            break
# 4.释放资源
capture.release()
# 5.关闭窗口
cv2.destroyAllWindows()