#!/bin/bash

# 切换到指定目录
cd /home/pi/Desktop/xct/motion-counting-raspberrypi

# 检查目录切换是否成功
if [ $? -eq 0 ]; then
    echo "已成功切换到目录：$(pwd)"
else
    echo "目录切换失败，请检查路径是否正确"
    exit 1
fi

# 激活虚拟环境
source ~/yolo11/bin/activate

# 检查虚拟环境是否激活成功
if [ $? -eq 0 ]; then
    echo "虚拟环境 'yolo11' 已激活"
else
    echo "虚拟环境激活失败，请检查路径是否正确"
    exit 1
fi

# 执行 Python 脚本
python my_yolo_interface.py

# 检查 Python 脚本执行是否成功
if [ $? -eq 0 ]; then
    echo "Python 脚本 'my_yolo_interface.py' 执行成功"
else
    echo "Python 脚本 'my_yolo_interface.py' 执行失败"
fi