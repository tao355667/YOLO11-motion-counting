# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '最小播放器.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionasdasd = QAction(MainWindow)
        self.actionasdasd.setObjectName(u"actionasdasd")
        self.actionasd = QAction(MainWindow)
        self.actionasd.setObjectName(u"actionasd")
        self.actionasd_2 = QAction(MainWindow)
        self.actionasd_2.setObjectName(u"actionasd_2")
        self.actiona = QAction(MainWindow)
        self.actiona.setObjectName(u"actiona")
        self.actionsd = QAction(MainWindow)
        self.actionsd.setObjectName(u"actionsd")
        self.actionas = QAction(MainWindow)
        self.actionas.setObjectName(u"actionas")
        self.actiond = QAction(MainWindow)
        self.actiond.setObjectName(u"actiond")
        self.actionasd_3 = QAction(MainWindow)
        self.actionasd_3.setObjectName(u"actionasd_3")
        self.actionasd_4 = QAction(MainWindow)
        self.actionasd_4.setObjectName(u"actionasd_4")
        self.actiona_2 = QAction(MainWindow)
        self.actiona_2.setObjectName(u"actiona_2")
        self.actionsd_2 = QAction(MainWindow)
        self.actionsd_2.setObjectName(u"actionsd_2")
        self.actionas_2 = QAction(MainWindow)
        self.actionas_2.setObjectName(u"actionas_2")
        self.actiond_2 = QAction(MainWindow)
        self.actiond_2.setObjectName(u"actiond_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self._video_widget = QVideoWidget(self.centralwidget)
        self._video_widget.setObjectName(u"_video_widget")
        self._video_widget.setGeometry(QRect(40, 20, 721, 511))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menusad = QMenu(self.menubar)
        self.menusad.setObjectName(u"menusad")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menusad.menuAction())
        self.menusad.addAction(self.actionasdasd)
        self.menusad.addAction(self.actionasd)
        self.menusad.addAction(self.actionasd_2)
        self.menusad.addAction(self.actiona)
        self.menusad.addAction(self.actionsd)
        self.menusad.addAction(self.actionas)
        self.menusad.addAction(self.actiond)
        self.menusad.addAction(self.actionasd_3)
        self.menusad.addAction(self.actionasd_4)
        self.menusad.addAction(self.actiona_2)
        self.menusad.addAction(self.actionsd_2)
        self.menusad.addAction(self.actionas_2)
        self.menusad.addAction(self.actiond_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionasdasd.setText(QCoreApplication.translate("MainWindow", u"asdasd", None))
        self.actionasd.setText(QCoreApplication.translate("MainWindow", u"asd", None))
        self.actionasd_2.setText(QCoreApplication.translate("MainWindow", u"asd", None))
        self.actiona.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.actionsd.setText(QCoreApplication.translate("MainWindow", u"sd", None))
        self.actionas.setText(QCoreApplication.translate("MainWindow", u"as", None))
        self.actiond.setText(QCoreApplication.translate("MainWindow", u"d", None))
        self.actionasd_3.setText(QCoreApplication.translate("MainWindow", u"asd", None))
        self.actionasd_4.setText(QCoreApplication.translate("MainWindow", u"asd", None))
        self.actiona_2.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.actionsd_2.setText(QCoreApplication.translate("MainWindow", u"sd", None))
        self.actionas_2.setText(QCoreApplication.translate("MainWindow", u"as", None))
        self.actiond_2.setText(QCoreApplication.translate("MainWindow", u"d", None))
        self.menusad.setTitle(QCoreApplication.translate("MainWindow", u"sad", None))
    # retranslateUi

