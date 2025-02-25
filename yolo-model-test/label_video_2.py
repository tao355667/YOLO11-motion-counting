from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt
import cv2

app = QtWidgets.QApplication([])


label = QtWidgets.QLabel()
label_output = QtWidgets.QLabel()
label.setGeometry(QtCore.QRect(100, 180, 500, 500))
label_output.setGeometry(QtCore.QRect(600, 180, 500, 500))

video_path = "./video/深蹲.mp4"
video = cv2.VideoCapture(video_path)
# 获取输入视频的宽度
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
# 获取输入视频的高度
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 获取视频帧数
frame_number = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
# 获取输入视频的帧率
frame_rate = int(video.get(cv2.CAP_PROP_FPS))

ratio1 = width / 500  # (label 宽度)
ratio2 = height / 500  # (label 高度)
ratio = max(ratio1, ratio2)

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    # 将BGR格式的帧转换为RGB格式
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 显示原始视频
    # 将图片转换为 Qt 格式
    # QImage:QImage(bytes,width,height,format)
    picture = QtGui.QImage(frame_rgb, width, height, 3 * width, QtGui.QImage.Format_RGB888)
    pixmap = QtGui.QPixmap.fromImage(picture)
    # 按照缩放比例自适应 label 显示
    pixmap.setDevicePixelRatio(ratio)
    label.setPixmap(pixmap)
    label.show()
    # 显示处理后的视频
    picture = QtGui.QImage(frame, width, height, 3 * width, QtGui.QImage.Format_RGB888)
    pixmap = QtGui.QPixmap.fromImage(picture)
    # 按照缩放比例自适应 label 显示
    pixmap.setDevicePixelRatio(ratio)
    label_output.setPixmap(pixmap)
    label_output.show()
    cv2.waitKey(10)

video.release()  # 释放资源
app.exec()
