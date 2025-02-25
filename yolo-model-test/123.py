import sys

from Ui_最小播放器 import Ui_MainWindow
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._player.setVideoOutput(self.ui._video_widget)

    def play(self):
        fp = './video/俯卧撑.mp4'
        self._player.setSource(QUrl.fromLocalFile(fp))
        self._player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.setWindowTitle("Min_Player")
    main_win.show()
    main_win.play()
    sys.exit(app.exec())
