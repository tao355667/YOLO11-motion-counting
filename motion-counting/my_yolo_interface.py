'''
yolo类，用于处理视频中的运动检测
'''
import os
import cv2

from ultralytics import solutions


class yolo_workouts():
    def __init__(self):
        self.motion_dic = {
            # 检测右肩、右肘、右手
            "俯卧撑-上": {"point_list": [6, 8, 10], "up_angle": 131.0, "down_angle": 89.0},
            # 检测左肩、左肘、左手
            "俯卧撑-左": {"point_list": [5, 7, 9], "up_angle": 131.0, "down_angle": 89.0},
            # 检测右肩、右肘、右手
            "俯卧撑-右": {"point_list": [6, 8, 10], "up_angle": 131.0, "down_angle": 89.0},
            # 检测左腰、左膝、左脚
            "深蹲-左": {"point_list": [11, 13, 15], "up_angle": 131.0, "down_angle": 89.0},
            # 检测右腰、右膝、右脚
            "深蹲-右": {"point_list": [12, 14, 16], "up_angle": 131.0, "down_angle": 89.0},
            # 检测右肩、右肘、右手
            "引体向上": {"point_list": [6, 8, 10], "up_angle": 131.0, "down_angle": 89.0},
            # 检测左肩、左腰、左膝
            "仰卧起坐-左": {"point_list": [5, 11, 13], "up_angle": 115.0, "down_angle": 85.0},
            # 检测右肩、右腰、右膝
            "仰卧起坐-右": {"point_list": [6, 12, 14], "up_angle": 115.0, "down_angle": 85.0}
        }
        self.model_dic = {
            "ncnn-n": "./weights/yolo11n-pose_ncnn_model",
            "ncnn-s": "./weights/yolo11s-pose_ncnn_model",
            ".pt-n": "./weights/yolo11n-pose.pt",
            ".pt-s": "./weights/yolo11s-pose.pt",
            ".pt-m": "./weights/yolo11m-pose.pt",
            ".pt-l": "./weights/yolo11l-pose.pt",
            ".pt-x": "./weights/yolo11x-pose.pt",
            ".onnx-n": "./weights/yolo11n-pose.onnx",
            ".onnx-s": "./weights/yolo11s-pose.onnx",
            ".onnx-m": "./weights/yolo11m-pose.onnx",
            ".onnx-l": "./weights/yolo11l-pose.onnx",
            ".onnx-x": "./weights/yolo11x-pose.onnx",
        }

    def set_model_video(self, model_name, video_path):
        """
        设置模型和视频路径
        """
        self.set_model_video_path(self.model_dic[model_name], video_path)

    def set_model_video_path(self, model_path, video_path=""):
        """
        设置参数
        """
        self.model_path = model_path  # 模型路径
        self.video_path = video_path  # 视频路径

    def set_motion_type(self, motion_type, show=False, verbose=False):
        """
        设置运动类型
        """
        print(f"motion_type: {motion_type}")
        # 如果运动类型在字典索引中
        if motion_type in self.motion_dic:
            # debug这些输入的参数
            # print(f"motion_type: {motion_type}")
            # print(f"point_list: {self.motion_dic[motion_type]['point_list']}")
            # print(f"up_angle: {self.motion_dic[motion_type]['up_angle']}")
            # print(f"down_angle: {self.motion_dic[motion_type]['down_angle']}")
            self.set_model(self.motion_dic[motion_type]["point_list"], self.motion_dic[motion_type]
                           ["up_angle"], self.motion_dic[motion_type]["down_angle"], show, verbose)

    def set_model(self, point_list, up_angle=131.0, down_angle=89.0, show=False, verbose=False):
        '''
        设置模型
        '''

        self.point_list = point_list  # 运动需要哪些节点
        self.up_angle = up_angle  # 上角度
        self.down_angle = down_angle  # 下角度
        self.show = show  # 是否显示视频
        self.gym = solutions.AIGym(
            model=self.model_path,  # 指定模型的路径
            show=self.show,  # 控制是否显示训练过程
            line_width=2,  # 设置线条的宽度
            up_angle=self.up_angle,  # 设置向上的角度
            down_angle=self.down_angle,  # 设置向下的角度
            kpts=self.point_list,  # 设置关键点列表
            verbose=verbose  # 关闭调试信息
        )

    def detect_image(self, img):
        """
        单张图片检测
        """
        img_output = self.gym.monitor(img)
        return img_output, self.gym.angle, self.gym.count, self.gym.stage

    def detect_video(self):
        """
        视频检测
        """
        # 使用OpenCV读取视频文件
        cap = cv2.VideoCapture(self.video_path)
        # 检查视频文件是否成功打开
        assert cap.isOpened(), "Error reading video file"
        # 获取视频的宽度、高度和帧率
        w, h, fps = (int(cap.get(x))
                     for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
        # 遍历视频帧
        while cap.isOpened():
            success, im0 = cap.read()  # 读取视频中的一帧
            # 显示帧
            # cv2.imshow("video", im0)
            # cv2.waitKey(1)
            if not success:
                # 如果读取失败，打印提示信息并退出循环
                print("Video frame is empty or video processing has been successfully completed.")
                break
            # 处理当前帧
            im0, angle_data, count_data, stage_data = self.detect_image(im0)
            # 输出信息  角度，数量，阶段（上升/下降）
            print(f"Angle: {angle_data} Count: {count_data} stage: {stage_data}")
        # 释放所有窗口
        cv2.destroyAllWindows()


def run_model_motion_video(model_name, motion_type, video_path, show=False, verbose=False):
    model = yolo_workouts()
    model.set_model_video(model_name=model_name, video_path=video_path)
    model.set_motion_type(motion_type=motion_type, show=show, verbose=verbose)
    model.detect_video()


if __name__ == '__main__':
    # run_model_motion_video(".pt-n", "俯卧撑-上", "./video/俯卧撑-上.mp4", show=True, verbose=True)
    # run_model_motion_video(".pt-n", "俯卧撑-左", "./video/俯卧撑-左.mp4", show=True, verbose=True)
    # run_model_motion_video(".pt-n", "俯卧撑-右", "./video/俯卧撑-右.mp4", show=True, verbose=True)

    # run_model_motion_video(".pt-n", "深蹲-左", "./video/深蹲-左.mp4", show=True, verbose=True)
    # run_model_motion_video(".pt-n", "深蹲-右", "./video/深蹲-右.mp4", show=True, verbose=True)

    # run_model_motion_video(".pt-n", "引体向上", "./video/引体向上.mp4", show=True, verbose=True)

    # run_model_motion_video(".pt-n", "仰卧起坐-左", "./video/仰卧起坐-左.mp4", show=True, verbose=True)
    run_model_motion_video(".onnx-n", "仰卧起坐-右", "./video/仰卧起坐-右 (2).mp4", show=True, verbose=True)
    # run_model_motion_video("ncnn-n", "仰卧起坐-右", "./video/仰卧起坐-右 (2).mp4", show=True, verbose=True)
