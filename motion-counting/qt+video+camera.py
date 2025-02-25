'''
TODO：没有加推理，只是显示视频，之后再写个yolo类，加到这个里面即可
'''

from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QApplication
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap
from Ui_motion_counting import Ui_MainWindow
import cv2
import os
import qdarktheme
from threading import Thread
import time


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化UI
        self.init_sth()  # 初始化一些自己的东西
        self.init_camera()  # 初始化摄像头
        self.bind()  # 绑定事件

    def init_camera(self):
        # 定义定时器，用于控制显示视频的帧率
        self.timer_camera = QTimer()
        # 定时到了，回调 self.show_camera
        self.timer_camera.timeout.connect(self.show_camera)
        # 要处理的视频帧图片队列，目前就放1帧图片
        self.frameToAnalyze = []
        # 启动处理视频帧独立线程
        Thread(target=self.frameAnalyzeThreadFunc, daemon=True).start()

    def init_sth(self):
        '''
        初始化一些自己的东西
        '''
        self.clear_angel_count_stage()
        print(f'angel: {self.angel}, count: {self.count}, stage: {self.stage}')
        self.statusBar().showMessage("状态：")
        self.cap = None  # 初始化cap属性为None
        self.video_path = ""   # 初始化视频路径
        self.set_filepath()
        self.file_is_playing = True  # 默认状态设置为播放

    def set_filepath(self):
        '''
        设置文件路径
        '''
        if self.video_path:  # 检查文件名是否为空
            self.label_filepath.setText(self.video_path)  # 显示文件路径
        else:
            self.label_filepath.setText("未选择文件")  # 显示文件路径

    def clear_angel_count_stage(self):
        self.angel = []
        self.count = []
        self.stage = []

    def bind(self):
        '''
        绑定事件
        '''
        self.pushButton_start.clicked.connect(self.start_video)
        self.pushButton_videofile.clicked.connect(self.open_videofile)
        self.pushButton_stop.clicked.connect(self.stop_video)
        self.pushButton_stop.clicked.connect(self.stop_camera)
        self.pushButton_camera.clicked.connect(self.startCamera)

    def stop_video(self):
        '''
        停止视频
        '''
        print("==debug==>停止视频")
        self.file_is_playing = False
        # self.stop_camera()
        pass

    def open_videofile(self):
        '''
        打开视频文件
        '''
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)  # 设置为选择已有的文件
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mov *.mkv);;All Files (*)")  # 设置文件过滤器
        file_dialog.setViewMode(QFileDialog.List)  # 设置视图模式

        if file_dialog.exec():  # 如果用户选择了文件并点击了“打开”
            file_paths = file_dialog.selectedFiles()  # 获取选择的文件路径
            print(f"选择的文件路径: {file_paths}")  # 输出选择的文件路径
            if file_paths:
                self.video_path = file_paths[0]  # 只取第一个文件路径
                if self.video_path:  # 检查文件名是否为空
                    self.statusBar().showMessage(f"状态：文件 {self.video_path} 被选择")
                    print(f"选择的视频文件路径: {self.video_path}")  # 输出选择的路径
                    self.set_filepath()  # 显示文件路径
                else:
                    self.statusBar().showMessage("状态："+"选择的文件路径为空")  # 文件名为空的提示
            else:
                self.statusBar().showMessage("状态："+"未选择文件")  # 没有选择文件的提示
        else:
            # print(f'self.video_path: {self.video_path}')
            self.statusBar().showMessage("状态："+"未选择文件")  # 取消选择文件的提示

    def start_video(self):
        '''
        播放视频
        '''
        self.stop_camera()  # 先停止摄像头
        print("==debug==>播放视频")
        if not self.video_path:
            self.statusBar().showMessage("状态："+"请先选择视频文件")
            # 弹出对话框，提示用户选择视频文件
            QMessageBox.warning(self, "警告", "请先选择视频文件", QMessageBox.Ok)
            return

        # video_path = "./video/深蹲.mp4"
        video = cv2.VideoCapture(self.video_path)
        if video.isOpened():
            self.statusBar().showMessage("状态："+"文件 "+self.video_path+" 打开成功")
        else:
            self.statusBar().showMessage("状态："+"文件 "+self.video_path+" 打开失败")
        # 获取输入视频的宽度
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        # 获取输入视频的高度
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # 获取视频帧数
        frame_number = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        # 获取输入视频的帧率
        frame_rate = int(video.get(cv2.CAP_PROP_FPS))

        ratio1 = width / self.video_input.width()  # (label 宽度)
        ratio2 = height / self.video_input.width()  # (label 高度)
        ratio = max(ratio1, ratio2)
        print(f'ratio: {ratio}')
        self.file_is_playing = True  # 默认状态设置为播放

        # 视频输出路径
        out_path = "./runs/" + os.path.splitext(os.path.basename(self.video_path))[0] + ".avi"
        # 创建一个视频写入对象，用于将处理后的视频保存为.avi文件
        video_writer = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(
            *"mp4v"), frame_rate, (width, height))
        while video.isOpened() and self.file_is_playing:
            self.statusBar().showMessage("状态："+"文件 "+self.video_path+" 播放中")
            ret, frame = video.read()
            if not ret:
                break
            # 将BGR格式的帧转换为RGB格式
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # 显示原始视频
            # 将图片转换为 Qt 格式
            # QImage:QImage(bytes,width,height,format)
            picture = QImage(frame_rgb, width, height, 3 * width, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(picture)
            # 按照缩放比例自适应 label 显示
            pixmap.setDevicePixelRatio(ratio)
            self.video_input.setPixmap(pixmap)
            self.video_input.show()

            # 显示处理后的视频
            yolo_output = self.yolo11_detect(frame)  # yolo11前向计算
            # print(f'==debug==>yolo_output: {yolo_output.shape} yolo_output.dtype: {yolo_output.dtype}')
            if self.radioButton_saveoutput.isChecked():  # 保存视频
                video_writer.write(cv2.cvtColor(yolo_output, cv2.COLOR_RGB2BGR))  # 将处理后的帧写入输出视频
            outpicture = QImage(yolo_output, width, height, 3 * width, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(outpicture)
            # 按照缩放比例自适应 label 显示
            pixmap.setDevicePixelRatio(ratio)
            self.video_output.setPixmap(pixmap)
            self.video_output.show()
            cv2.waitKey(10)
            # delay = 1000 / 60  # 60 FPS
            # cv2.waitKey(int(delay))
        video.release()  # 释放资源
        video_writer.release()  # 释放视频写入对象
        if self.file_is_playing:
            self.statusBar().showMessage("状态："+"文件 "+self.video_path+" 播放完毕")
        else:
            self.video_input.clear()  # 清空视频显示区域
            self.video_output.clear()  # 清空视频显示区域
            self.statusBar().showMessage("状态："+"文件 "+self.video_path+" 播放停止")

    def startCamera(self):
        # 参考 https://docs.opencv.org/3.4/dd/d43/tutorial_py_video_display.html
        # 在 windows上指定使用 cv2.CAP_DSHOW 会让打开摄像头快很多，
        # 在 Linux/Mac上 指定 V4L, FFMPEG 或者 GSTREAMER
        self.stop_video()  # 先停止播放视频
        print("==debug==>播放摄像头")
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not self.cap.isOpened():
            print("1号摄像头不能打开")
            return ()

        if self.timer_camera.isActive() == False:  # 若定时器未启动
            self.timer_camera.start(50)

    def show_camera(self):
        '''
        播放摄像头
        '''

        ret, frame = self.cap.read()  # 从视频流中读取
        if not ret:
            return
        # height, width, channels = frame.shape
        # print(f"帧的高度: {height}, 帧的宽度: {width}")
        # ratio1 = width / self.video_input.width()  # (label 宽度)
        # ratio2 = height / self.video_input.width()  # (label 高度)
        # ratio = max(ratio1, ratio2)
        # 把读到的16:10帧的大小重新设置
        frame = cv2.resize(frame, (640, 480))
        # 视频色彩转换回RGB，OpenCV images as BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        qImage = QImage(frame.data, frame.shape[1], frame.shape[0],
                        QImage.Format_RGB888)  # 变成QImage形式

        pixmap = QPixmap.fromImage(qImage)
        # 按照缩放比例自适应 label 显示
        # pixmap.setDevicePixelRatio(ratio)
        self.video_input.setPixmap(pixmap)
        self.video_input.show()
        # 往显示视频的Label里 显示QImage
        # self.video_input.setPixmap(QPixmap.fromImage(qImage))
        # 如果当前没有处理任务
        if not self.frameToAnalyze:
            self.frameToAnalyze.append(frame)
        pass

    def stop_camera(self):
        print("==debug==>停止摄像头")
        self.timer_camera.stop()  # 关闭定时器
        if self.cap is not None:
            self.cap.release()  # 释放视频流
        self.video_input.clear()  # 清空视频显示区域
        self.video_output.clear()  # 清空视频显示区域

    def frameAnalyzeThreadFunc(self):

        while True:
            # print("==debug==>frameAnalyzeThreadFunc")
            if not self.frameToAnalyze:
                time.sleep(0.01)
                continue

            frame = self.frameToAnalyze.pop(0)

            # results = self.model(frame)[0]
            # results = frame
            # results = self.yolo11_detect(frame)

            # img = results.plot(line_width=1)

            # qImage = QImage(img.data, img.shape[1], img.shape[0],
            #                 QImage.Format_RGB888)  # 变成QImage形式

            # self.video_output.setPixmap(QPixmap.fromImage(qImage))  # 往显示Label里 显示QImage

            # 我的
            # height, width, channels = frame.shape

            # ratio1 = width / self.video_input.width()  # (label 宽度)
            # ratio2 = height / self.video_input.width()  # (label 高度)
            # ratio = max(ratio1, ratio2)
            # 把读到的16:10帧的大小重新设置
            frame = cv2.resize(frame, (640, 480))
            # 视频色彩转换回RGB，OpenCV images as BGR
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            qImage = QImage(frame.data, frame.shape[1],
                            frame.shape[0], QImage.Format_RGB888)  # 变成QImage形式

            pixmap = QPixmap.fromImage(qImage)
            # 按照缩放比例自适应 label 显示
            # pixmap.setDevicePixelRatio(ratio)
            self.video_output.setPixmap(pixmap)
            self.video_output.show()

            # time.sleep(0.5)

    def yolo11_detect(self, img):
        # print("==debug==>yolo检测")

        return img


def main():
    app = QApplication()
    qdarktheme.setup_theme("light")  # 美化页面
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
