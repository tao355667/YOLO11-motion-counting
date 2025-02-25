# 基于yolo11的健身计系统

## 搭建环境

1. python version: 3.11.10
2. install pytorch(my command:`pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124`)
3. install other packages : `pip install -r requirements.txt`

## 导出环境

`pip freeze > requirements.txt`

## pyinstaller 打包

pyinstaller main.py

pyinstaller -w -i logo.ico main.py

这个打包后有 5.47 个 G，太大了，而且运行起来也卡。。
