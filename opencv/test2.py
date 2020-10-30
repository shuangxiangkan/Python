import cv2 as cv


def image_show():
    image=cv.imread("C:/Users/Kansx/Pictures/Saved Pictures/3063.jpg")
    cv.imshow("image_input",image)
    cv.waitKey(0)
    cv.destroyAllWindows()


def video_show():
    capture=cv.VideoCapture(0)
    while True:
        ret,frame=capture.read()
        frame=cv.flip(frame,0)
        cv.imshow("video_show_output",frame)
        c=cv.waitKey(50)
        if c==27:
            break
    cv.destroyAllWindows()


# image_show()
video_show()