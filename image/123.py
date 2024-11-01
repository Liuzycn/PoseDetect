import numpy as np
import pyttsx3
import time
yuyin = pyttsx3.init()
def get_points(results):
    count = 0
    num = 0
    all_num = []
    flip_list = []
    coords=np.array(results.pose_landmarks.landmark)
    #汇总所有点的XYZ坐标
    def get_x(each):
        return each.x
    def get_y(each):
        return each.y
    def get_z(each):
        return each.z
    #分别获取关键点XYZ坐标
    points_x=np.array(list(map(get_x,coords)))
    points_y=np.array(list(map(get_y,coords)))
    points_z=np.array(list(map(get_z,coords)))
    #将三个方向坐标合并
    points=np.vstack((points_x,points_y,points_z)).T
    return points[0][1]
[4]
import cv2
import mediapipe as mp
from tqdm import tqdm
import time

# 导入solutions
mp_pose = mp.solutions.pose
# 导入绘图函数
mp_drawing = mp.solutions.drawing_utils
# 导入模型
pose = mp_pose.Pose(static_image_mode=True,  # 是静态还是连续视频帧
                    model_complexity=2,  # 选择人体姿态关键点检测模型，0性能差但快，2性能好但慢，1介于两者之间
                    smooth_landmarks=True,  # 选择平滑关键点
                    enable_segmentation=True,  # 是否人体抠图
                    min_detection_confidence=0.5,  # 置信度阈值
                    min_tracking_confidence=0.5)  # 追踪阈值
[40]
def countytxs():
    flag = False
    count = 0
    num = 0
    x = []
    y = []
    count_list = [0]
    # 调用摄像头，传入0表示获取系统默认摄像头
    cap = cv2.VideoCapture(0)
    # 打开cap
    cap.open(0)
    fp = 1
    i=-1
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 13, (640, 480))
    #start_time = time.time()
    #print(start_time)
    #time.sleep(interval)
    # 无限循环，直到break被触发
    while cap.isOpened():
        # 获取画面
        success, frame = cap.read()
        if success:
            if (fp==1):
                #time.sleep(interval)
                print('原地深蹲，一组60秒')
                yuyin.say('原地深蹲，一组60秒')
                yuyin.runAndWait()
                print('3,2,1,开始~')
                yuyin.say('3,2,1,开始~')
                yuyin.runAndWait()
                start_time = time.time()
                fp = 0
            else:
                #print(num)
                #frame = cv2.flip(frame, 1)

                end_time = time.time()
                #print(end_time)
                if end_time - start_time >= 60:
                    break
        else:
            print('Error')
            break
        ##！！！处理帧函数
        # frame = process_frame(frame)
        img_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 将RGB图像输入模型，获取预测结果
        results = pose.process(img_RGB)
        h, w = frame.shape[0], frame.shape[1]
        try:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            for i in range(33):  # 遍历33个关键点
                # 获取该关键点的三维坐标
                cx = int(results.pose_landmarks.landmark[i].x * w)
                cy = int(results.pose_landmarks.landmark[i].y * h)
                cz = results.pose_landmarks.landmark[i].z
                radius = 5
                if i == 0:  # 鼻尖
                    img = cv2.circle(frame, (cx, cy), radius, (0, 0, 255), -1)
                elif i in [11, 12]:  # 肩膀
                    img = cv2.circle(frame, (cx, cy), radius, (233, 155, 6), -1)
                elif i in [23, 24]:  # 踝关节
                    img = cv2.circle(frame, (cx, cy), radius, (1, 240, 255), -1)
                elif i in [13, 14]:  # 胳膊肘
                    img = cv2.circle(frame, (cx, cy), radius, (140, 47, 240), -1)
                elif i in [25, 26]:  # 膝盖
                    img = cv2.circle(frame, (cx, cy), radius, (0, 0, 255), -1)
                elif i in [15, 16, 27, 28]:  # 手腕和脚腕
                    img = cv2.circle(frame, (cx, cy), radius, (223, 155, 60), -1)
                elif i in [17, 19, 21]:  # 左手
                    img = cv2.circle(frame, (cx, cy), radius, (94, 218, 121), -1)
                elif i in [18, 20, 22]:  # 右手
                    img = cv2.circle(frame, (cx, cy), radius, (16, 144, 247), -1)
                elif i in [27, 29, 31]:  # 左脚
                    img = cv2.circle(frame, (cx, cy), radius, (29, 123, 243), -1)
                elif i in [28, 30, 32]:  # 右脚
                    img = cv2.circle(frame, (cx, cy), radius, (193, 182, 255), -1)
                elif i in [9, 10]:  # 嘴
                    img = cv2.circle(frame, (cx, cy), radius, (205, 235, 255), -1)
                elif i in [1, 2, 3, 4, 5, 6, 7, 8]:  # 眼及脸颊
                    img = cv2.circle(frame, (cx, cy), radius, (94, 218, 121), -1)
                else:  # 肩膀
                    img = cv2.circle(frame, (cx, cy), radius, (0, 255, 0), -1)
            point = get_points(results)
            y.append(point)
            x.append(num)
            num += 1
            print(num)
            if len(y) < 2:
                continue
            pre_point = y[len(y) - 2]
            if point > pre_point and point - pre_point >= 0.15:
                flag =  True
            if point < pre_point and flag == True and pre_point - point>= 0.15:
                count = count+1
                flag = False
            else:
                pass
        except:
            pass
        # 展示处理后的三通道图像
        cv2.putText(frame, str(count), (450, 100), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (0, 0, 255), 2)
        out.write(frame)
        cv2.imshow('my_window', frame)
        #end_time = time.time()
        #if num == 100:
        #if end_time - start_time == 60:  # 按键盘上的q或esc退出（在英文输入法下）
        if cv2.waitKey(1) in [ord('q'), 27]:
            break
    # 关闭摄像头
    cap.release()
    # 关闭图像窗口
    print('一分钟时间到')
    yuyin.say('一分钟时间到')
    yuyin.runAndWait()
    # 关闭图像窗口
    cv2.destroyAllWindows()
    print('运动结束，放松一下吧~')
    yuyin.say('运动结束，放松一下吧~')
    yuyin.say("您本次深蹲运动做了"f'{count}'"个，继续加油~")
    yuyin.runAndWait()
    return x,y,count
[42]
import math
from matplotlib import pyplot as plt
import numpy as np
import os
from scipy import signal
from scipy.signal import find_peaks

def LabberRing(x,y):
    plt.figure(figsize=(12, 10))
    # Input signal
    t=np.array(x)
    series = np.array(y)
    # Threshold value (for height of peaks and valleys)
    thresh = 0.5
    # Find indices of peaks
    peak_idx, _ = find_peaks(series, height=thresh)
    plt.plot([min(t), max(t)], [thresh, thresh], '--')

    # Plot signal
    plt.plot(t, series,'k')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(f"point numbers: {count}")
    # plt.grid()网格线设置
    plt.grid(True)
    plt.savefig("figure_2.png")
    plt.show()
    return


if __name__ == "__main__":
    x, y ,count= countytxs()
    plt.figure(figsize=(12, 10))
    #count = get_count(x, y)
    LabberRing(x, y)
