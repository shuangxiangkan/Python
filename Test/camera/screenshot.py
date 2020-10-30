import cv2
import time

# 获取本地摄像头
# folder_path 截取图片的存储目录
def get_img_from_camera_local(folder_path):
    cap = cv2.VideoCapture(0)
    i = 1
    while True:
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        # time.sleep(5)
        print(str(i))
        cv2.imwrite(folder_path + str(i) + '.jpg', frame)  # 存储为图像
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        i += 1
    cap.release()
    cv2.destroyAllWindows()

folder_path="/imgage/"
get_img_from_camera_local(folder_path)