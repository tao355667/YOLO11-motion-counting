'''
@author: xct
@date: 2024/12/5
@description: 导出YOLO模型为onnx和ncnn模型
有时运行1次无法得到所有权重文件，多跑几次就行了。
'''
from ultralytics import YOLO
import os

ptlFile = ["yolo11n-pose", "yolo11s-pose", "yolo11m-pose", "yolo11l-pose", "yolo11x-pose"]

# 导出onnx模型
for file in ptlFile:
    # 当前文件夹中没有file.onnx文件，则解压模型
    if not os.path.exists(file+".onnx"):
        print("==========>正在转换为onnx："+file)
        model = YOLO(file+".pt")  # Load a model
        model.export(format="onnx")  # Export the model

# 导出ncnn模型.只对 YOLO11n 和 YOLO11s 型号进行转换，因为其他型号尺寸太大，无法在 Raspberry Pis 上运行，也无法提供良好的性能。
for file in ptlFile[0:2]:
    # 当前文件夹中没有ncnn文件，则解压模型
    if not os.path.exists(file+"_ncnn_model"):
        print("==========>正在转换为ncnn："+file)
        model = YOLO(file+".pt")  # Load a model
        model.export(format="ncnn")  # Export the model
