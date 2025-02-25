import os
import cv2

from ultralytics import solutions


def workouts(model_path, video_path, point_list, up_angle=131.0, down_angle=89.0, show=True):
    # 使用OpenCV读取视频文件
    cap = cv2.VideoCapture(video_path)
    # 检查视频文件是否成功打开
    assert cap.isOpened(), "Error reading video file"

    # 获取视频的宽度、高度和帧率
    w, h, fps = (int(cap.get(x))
                 for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    # 视频输出路径
    out_path = "./runs/" + os.path.splitext(os.path.basename(video_path))[0] + ".avi"
    # 创建一个视频写入对象，用于将处理后的视频保存为.avi文件
    video_writer = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    # 创建一个AIGym实例，用于进行运动计数和模型测试
    gym = solutions.AIGym(
        model=model_path,  # 指定模型的路径
        show=False,  # 控制是否显示训练过程
        line_width=2,  # 设置线条的宽度
        up_angle=up_angle,  # 设置向上的角度
        down_angle=down_angle,  # 设置向下的角度
        kpts=point_list,  # 设置关键点列表
        verbose=False  # 关闭调试信息
    )

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
        # 使用监控对象处理当前帧
        im0 = gym.monitor(im0)
        # 将处理后的帧写入输出视频
        video_writer.write(im0)
        # 输出角度，数量，阶段（上升/下降）
        angle_data = gym.angle
        count_data = gym.count
        stage_data = gym.stage
        # 输出信息
        print(f"Angle: {angle_data} Count: {count_data} stage: {stage_data}")
        # print(type(angle_data))  # 输出信息的数据类型,都是list类型
        # print(type(count_data))  # 输出信息的数据类型
        # print(type(stage_data))  # 输出信息的数据类型
        # 输出信息的数据类型

    # 释放所有窗口
    cv2.destroyAllWindows()
    # 释放视频写入对象
    video_writer.release()


if __name__ == '__main__':
    # 选择模型
    model_pt = ["./weights/yolo11n-pose.pt", "./weights/yolo11s-pose.pt",
                "./weights/yolo11m-pose.pt", "./weights/yolo11l-pose.pt", "./weights/yolo11x-pose.pt"]
    model_onnx = ["./weights/yolo11n-pose.onnx", "./weights/yolo11s-pose.onnx",
                  "./weights/yolo11m-pose.onnx", "./weights/yolo11l-pose.onnx", "./weights/yolo11x-pose.onnx"]
    model_ncnn = ["./weights/yolo11n-pose_ncnn_model",
                  "./weights/yolo11n-pose_ncnn_model"]
    model_path = model_pt[3]  # 选择模型路径

    video_path = "./video/俯卧撑.mp4"
    point_list = [6, 8, 10]  # 头为正的俯卧撑，检测右肩、右肘、右手三个点形成的夹角。
    workouts(model_path, video_path, point_list)

    # video_path = "./video/俯卧撑1.mp4"
    # point_list = [5, 7, 9]  # 头为左的俯卧撑，检测左肩、左肘、左手三个点形成的夹角。
    # workouts(model_path, video_path, point_list)

    # video_path = "./video/俯卧撑2.mp4"
    # point_list = [6, 8, 10]  # 头为右的俯卧撑，检测右肩、右肘、右手三个点形成的夹角。
    # workouts(model_path, video_path, point_list)

    # video_path = "./video/引体向上1.mp4"
    # point_list = [6, 8, 10]  # 头为正的引体向上，检测右肩、右肘、右手三个点形成的夹角。
    # workouts(model_path, video_path, point_list)

    # video_path = "./video/引体卷腹.mp4"
    # point_list = [6, 12, 14]  # 右侧朝向的引体卷腹，检测右肩、右腰、右膝三个点形成的夹角。
    # workouts(model_path, video_path, point_list)

    # video_path = "./video/引体卷腹1.mp4"
    # point_list = [5, 11, 13]  # 左侧朝向的引体卷腹，检测左肩、左腰、左膝三个点形成的夹角。
    # workouts(model_path, video_path, point_list)

    # video_path = "./video/引体卷腹2.mp4"
    # point_list = [6, 12, 14]  # 正面朝向的引体卷腹，检测右肩、右腰、右膝三个点形成的夹角。
    # workouts(model_path, video_path, point_list)

    # video_path = "./video/仰卧起坐.mp4"
    # point_list = [6, 12, 14]  # 左侧朝向的仰卧起坐，检测右肩、右腰、右膝三个点形成的夹角。
    # workouts(model_path, video_path, point_list, down_angle=85)

    # video_path = "./video/V字卷腹.mp4"
    # point_list = [5, 11, 13]  # 右侧朝向的V字卷腹，检测左肩、左腰、左膝三个点形成的夹角。
    # workouts(model_path, video_path, point_list, up_angle=114)

    # video_path = "./video/深蹲.mp4"
    # point_list = [11, 13, 15]  # 左侧朝向的深蹲，检测左肩、左腰、左膝三个点形成的夹角。
    # workouts(model_path, video_path, point_list)
