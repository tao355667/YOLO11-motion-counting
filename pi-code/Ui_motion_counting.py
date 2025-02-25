# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'motion_counting.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSplitter,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1303, 742)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.video_input = QLabel(self.splitter)
        self.video_input.setObjectName(u"video_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.video_input.sizePolicy().hasHeightForWidth())
        self.video_input.setSizePolicy(sizePolicy1)
        self.video_input.setMinimumSize(QSize(640, 480))
        self.video_input.setSizeIncrement(QSize(0, 0))
        self.splitter.addWidget(self.video_input)
        self.video_output = QLabel(self.splitter)
        self.video_output.setObjectName(u"video_output")
        sizePolicy1.setHeightForWidth(self.video_output.sizePolicy().hasHeightForWidth())
        self.video_output.setSizePolicy(sizePolicy1)
        self.video_output.setMinimumSize(QSize(640, 480))
        self.video_output.setBaseSize(QSize(0, 0))
        self.splitter.addWidget(self.video_output)

        self.verticalLayout_3.addWidget(self.splitter)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy2)
        self.label_1.setMinimumSize(QSize(90, 0))
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_1)

        self.comboBox_model = QComboBox(self.centralwidget)
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.setObjectName(u"comboBox_model")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_model.sizePolicy().hasHeightForWidth())
        self.comboBox_model.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.comboBox_model)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(90, 0))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox_motion = QComboBox(self.centralwidget)
        self.comboBox_motion.addItem("")
        self.comboBox_motion.addItem("")
        self.comboBox_motion.addItem("")
        self.comboBox_motion.addItem("")
        self.comboBox_motion.addItem("")
        self.comboBox_motion.addItem("")
        self.comboBox_motion.addItem("")
        self.comboBox_motion.addItem("")
        self.comboBox_motion.setObjectName(u"comboBox_motion")
        sizePolicy3.setHeightForWidth(self.comboBox_motion.sizePolicy().hasHeightForWidth())
        self.comboBox_motion.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.comboBox_motion)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.textEdit_explain = QTextEdit(self.centralwidget)
        self.textEdit_explain.setObjectName(u"textEdit_explain")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.textEdit_explain.sizePolicy().hasHeightForWidth())
        self.textEdit_explain.setSizePolicy(sizePolicy4)

        self.verticalLayout.addWidget(self.textEdit_explain)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_angel = QLabel(self.centralwidget)
        self.label_angel.setObjectName(u"label_angel")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setPointSize(25)
        self.label_angel.setFont(font)

        self.verticalLayout_2.addWidget(self.label_angel)

        self.label_count = QLabel(self.centralwidget)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setFont(font)

        self.verticalLayout_2.addWidget(self.label_count)

        self.label_stage = QLabel(self.centralwidget)
        self.label_stage.setObjectName(u"label_stage")
        self.label_stage.setFont(font)

        self.verticalLayout_2.addWidget(self.label_stage)

        self.pushButton_resetcount = QPushButton(self.centralwidget)
        self.pushButton_resetcount.setObjectName(u"pushButton_resetcount")

        self.verticalLayout_2.addWidget(self.pushButton_resetcount)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_videofile = QPushButton(self.centralwidget)
        self.pushButton_videofile.setObjectName(u"pushButton_videofile")
        font1 = QFont()
        font1.setPointSize(11)
        self.pushButton_videofile.setFont(font1)

        self.gridLayout.addWidget(self.pushButton_videofile, 0, 0, 1, 1)

        self.pushButton_camera = QPushButton(self.centralwidget)
        self.pushButton_camera.setObjectName(u"pushButton_camera")
        self.pushButton_camera.setFont(font1)

        self.gridLayout.addWidget(self.pushButton_camera, 1, 0, 1, 1)

        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setFont(font1)

        self.gridLayout.addWidget(self.pushButton_start, 2, 0, 1, 1)

        self.pushButton_stop = QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setFont(font1)

        self.gridLayout.addWidget(self.pushButton_stop, 3, 0, 1, 1)

        self.radioButton_saveoutput = QRadioButton(self.centralwidget)
        self.radioButton_saveoutput.setObjectName(u"radioButton_saveoutput")

        self.gridLayout.addWidget(self.radioButton_saveoutput, 2, 1, 1, 1)

        self.label_filepath = QLabel(self.centralwidget)
        self.label_filepath.setObjectName(u"label_filepath")

        self.gridLayout.addWidget(self.label_filepath, 0, 1, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1303, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8fd0\u52a8\u8ba1\u6570", None))
        self.video_input.setText(QCoreApplication.translate("MainWindow", u"video_input", None))
        self.video_output.setText(QCoreApplication.translate("MainWindow", u"video_output", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6a21\u578b\uff1a", None))
        self.comboBox_model.setItemText(0, QCoreApplication.translate("MainWindow", u".pt-n", None))
        self.comboBox_model.setItemText(1, QCoreApplication.translate("MainWindow", u".pt-s", None))
        self.comboBox_model.setItemText(2, QCoreApplication.translate("MainWindow", u".pt-m", None))
        self.comboBox_model.setItemText(3, QCoreApplication.translate("MainWindow", u".pt-l", None))
        self.comboBox_model.setItemText(4, QCoreApplication.translate("MainWindow", u".pt-x", None))
        self.comboBox_model.setItemText(5, QCoreApplication.translate("MainWindow", u".onnx-n", None))
        self.comboBox_model.setItemText(6, QCoreApplication.translate("MainWindow", u".onnx-s", None))
        self.comboBox_model.setItemText(7, QCoreApplication.translate("MainWindow", u".onnx-m", None))
        self.comboBox_model.setItemText(8, QCoreApplication.translate("MainWindow", u".onnx-l", None))
        self.comboBox_model.setItemText(9, QCoreApplication.translate("MainWindow", u".onnx-x", None))
        self.comboBox_model.setItemText(10, QCoreApplication.translate("MainWindow", u"ncnn-n", None))
        self.comboBox_model.setItemText(11, QCoreApplication.translate("MainWindow", u"ncnn-s", None))

        self.comboBox_model.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6a21\u578b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8fd0\u52a8\u9879\u76ee\uff1a", None))
        self.comboBox_motion.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4fef\u5367\u6491-\u4e0a", None))
        self.comboBox_motion.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4fef\u5367\u6491-\u5de6", None))
        self.comboBox_motion.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4fef\u5367\u6491-\u53f3", None))
        self.comboBox_motion.setItemText(3, QCoreApplication.translate("MainWindow", u"\u6df1\u8e72-\u5de6", None))
        self.comboBox_motion.setItemText(4, QCoreApplication.translate("MainWindow", u"\u6df1\u8e72-\u53f3", None))
        self.comboBox_motion.setItemText(5, QCoreApplication.translate("MainWindow", u"\u5f15\u4f53\u5411\u4e0a", None))
        self.comboBox_motion.setItemText(6, QCoreApplication.translate("MainWindow", u"\u4ef0\u5367\u8d77\u5750-\u5de6", None))
        self.comboBox_motion.setItemText(7, QCoreApplication.translate("MainWindow", u"\u4ef0\u5367\u8d77\u5750-\u53f3", None))

        self.comboBox_motion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u9879\u76ee", None))
        self.textEdit_explain.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8fd0\u52a8\u9879\u76ee\u7684\u671d\u5411\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8eab\u4f53\u8ddd\u79bb\u6444\u50cf\u5934\u8f83\u8fd1\u7684\u4e00\u4fa7\uff0c\u5982\u5de6\u81c2\u8ddd\u79bb\u6444\u50cf\u5934\u8fd1\uff0c\u5c31\u662f\u5de6\u4fa7</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-t"
                        "op:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6a21\u578b\u4ece\u5c0f\u5230\u5927\uff1an s m l x</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">pt\u53ef\u76f4\u63a5\u63a8\u7406</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ncnn\u9002\u5408\u6811\u8393\u6d3e\uff08yolo\u8bf4\u7684\uff09\uff0c\u4f46\u5b9e\u9645\u4e0a\u6548\u679c\u4e0d\u597d</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">onnx\u9700\u8981\u5728\u5168\u5c40python\u73af\u5883\u4e2d\u5b89\u88c5onnx\u5e93</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt"
                        "-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_angel.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u5ea6\uff1a", None))
        self.label_count.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u6570\uff1a", None))
        self.label_stage.setText(QCoreApplication.translate("MainWindow", u"\u9636\u6bb5\uff1a", None))
        self.pushButton_resetcount.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u6570\u6e05\u96f6", None))
        self.pushButton_videofile.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u89c6\u9891\u6587\u4ef6", None))
        self.pushButton_camera.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934\u5f00\u59cb", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u5f00\u59cb", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.radioButton_saveoutput.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8bc6\u522b\u7ed3\u679c\u89c6\u9891", None))
        self.label_filepath.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u9009\u62e9\u6587\u4ef6", None))
    # retranslateUi

