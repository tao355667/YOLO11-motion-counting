# 运动计数系统，部署到树莓派上

## 搭建环境

### venv创建虚拟环境

创建虚拟环境：`python3.11 -m venv ~/yolo11`

激活虚拟环境：`source ~/yolo11/bin/activate`

### 安装依赖包

**安装pytorch**

参考命令`pip3 install torch torchvision torchaudio`

**安装opencv**

`pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple`

**安装ultralytics**

`pip install ultralytics -i https://pypi.tuna.tsinghua.edu.cn/simple`

**安装numpy1.26.1(因为numpy2.x版本有bug)**

`pip install numpy==1.26.4 -i https://pypi.tuna.tsinghua.edu.cn/simple`


`pip install shapely==2.0.6 -i https://pypi.tuna.tsinghua.edu.cn/simple`

pip install onnx -i https://pypi.tuna.tsinghua.edu.cn/simple

onnxruntime（CPU版）

pip install onnxruntime -i https://pypi.tuna.tsinghua.edu.cn/simple


ultralytics需要这个版本的numpy

pip install numpy==1.23.5 -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install lapx==0.5.11 -i https://pypi.tuna.tsinghua.edu.cn/simple

## 导出环境

`pip freeze > requirements.txt`

## 运行程序


`source ~/yolo11/bin/activate`
`cd 你的文件目录`
`python3 my_yolo_interface.py`
