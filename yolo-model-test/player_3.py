import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QSlider, QFileDialog, QLabel
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl, Qt


class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("视频播放器")
        self.setGeometry(100, 100, 1024, 768)

        self.media_player = QMediaPlayer()
        self.video_widget = QVideoWidget()
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

        self.file_label = QLabel("当前播放: ")  # 创建标签显示当前播放的文件名
        self.file_label.setFixedHeight(20)  # 设置标签的固定高度，减少占用空间

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        layout.addWidget(self.file_label)  # 添加标签到布局
        layout.addWidget(self.select_button)  # 添加选择视频的按钮
        layout.addWidget(self.start_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.slider)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "选择视频文件", "", "视频文件 (*.mp4 *.avi *.mov *.mkv)")  # 选择视频文件
        if file_name:
            self.media_player.setSource(QUrl.fromLocalFile(file_name))  # 设置选中的视频文件
            self.file_label.setText(f"当前播放: {file_name}")  # 更新标签显示文件名
            self.start_video()

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
