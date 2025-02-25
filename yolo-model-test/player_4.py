import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QSlider, QFileDialog, QLabel
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QImage, QPixmap
import cv2


class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("视频播放器")
        self.setGeometry(100, 100, 1400, 768)  # 增加窗口宽度以容纳两个视频

        self.media_player = QMediaPlayer()
        self.video_widget = QVideoWidget()
        self.processed_video_widget = QVideoWidget()  # 用于显示处理后的视频
        self.media_player.setVideoOutput(self.video_widget)

        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)

        self.start_button = QPushButton("开始")
        self.start_button.clicked.connect(self.start_video)

        self.pause_button = QPushButton("暂停")
        self.pause_button.clicked.connect(self.pause_video)

        self.stop_button = QPushButton("停止")
        self.stop_button.clicked.connect(self.stop_video)

        self.select_button = QPushButton("选择视频")
        self.select_button.clicked.connect(self.open_file)

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.sliderMoved.connect(self.set_position)

        self.file_label = QLabel("当前播放: ")
        self.file_label.setFixedHeight(20)

        mainLayout = QVBoxLayout()  # 使用垂直布局
        # 视频显示布局
        layout_video = QHBoxLayout()  # 使用水平布局
        layout_video.addWidget(self.video_widget)  # 添加原始视频显示
        layout_video.addWidget(self.processed_video_widget)  # 添加处理后视频显示

        mainLayout.addLayout(layout_video)  # 添加视频显示布局
        mainLayout.addWidget(self.file_label)
        mainLayout.addWidget(self.select_button)
        mainLayout.addWidget(self.start_button)
        mainLayout.addWidget(self.pause_button)
        mainLayout.addWidget(self.stop_button)
        mainLayout.addWidget(self.slider)

        center_container = QWidget()
        center_container.setLayout(mainLayout)
        self.setCentralWidget(center_container)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "选择视频文件", "", "视频文件 (*.mp4 *.avi *.mov *.mkv)")
        if file_name:
            self.media_player.setSource(QUrl.fromLocalFile(file_name))
            # 处理视频，假设你有一个处理函数
            self.process_video(file_name)  # 在这里调用处理视频的函数
            self.file_label.setText(f"当前播放: {file_name}")
            self.start_video()

    def process_video(self, file_name):
        # 先不处理，将原始视频帧放在这里
        # 使用OpenCV打开视频文件
        cap = cv2.VideoCapture(file_name)

        if not cap.isOpened():
            print("无法打开视频文件")
            return

        while True:
            ret, frame = cap.read()  # 读取每一帧

            if not ret:
                break  # 如果没有帧可读，退出循环

            # 这里可以进行帧的处理，例如转换为灰度图像
            processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 将图像转换为QImage以便在Qt中使用
            height, width = processed_frame.shape
            qimg = QImage(processed_frame.data, width, height, width, QImage.Format_Grayscale8)

            # 在processed_video_widget上显示处理过的图像
            self.processed_video_widget.setPixmap(QPixmap.fromImage(qimg))

        cap.release()  # 释放视频捕获对象
        # 在这里添加处理视频的逻辑，处理后的视频应显示在processed_video_widget上
        # 你可能需要使用其他库（如OpenCV）来处理帧，然后将其传递给QMediaPlayer
        pass

    def start_video(self):
        self.media_player.play()

    def pause_video(self):
        self.media_player.pause()

    def stop_video(self):
        self.media_player.stop()

    def set_position(self, position):
        self.media_player.setPosition(position)

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    video_player = VideoPlayer()
    video_player.show()
    sys.exit(app.exec())
