import cv2 as cv

def video_demo():
    capture=cv.VideoCapture(0)
    while(True):
        ret,frame=capture.read()
        frame=cv.flip(frame,1)
        cv.imshow("video",frame)
        c=cv.waitKey(50)
        if c==27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


# print("-----Hello Python-----")
# src=cv.imread("C:/Users/Kansx/Pictures/Saved Pictures/3061.jpg")
# cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
# cv.imshow("input image",src)
# get_image_info(src)
# gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
# cv.imwrite("D:/result.png",gray)
video_demo()
cv.waitKey(0)

cv.destroyAllWindow()