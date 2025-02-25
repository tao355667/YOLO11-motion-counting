# 基于YOLO11-pose的运动计数系统


## 开发工具的选择

开发语言为Python，利用PySide6框架构建GUI，确保软件可以在Windows和Linux系统上运行。使用VS Code作为主要的代码编辑器，利用PySide6Designer和PySide6-UIC等工具进行界面设计和代码转换。

## 软件架构概述

本系统采用模块化设计，主要由UI界面类（Ui_MainWindow）、YOLO11接口类（yolo_workouts）和主程序类（MainWindow）三个类组成，实现了系统的功能并方便后续的维护和升级。

## 文件内容

项目文件：`motion-counting`
部署到树莓派上：`pi-code`
yolo模型测试文件：`yolo-model-test`