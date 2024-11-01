from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel,QMessageBox
from PyQt5.QtCore import QThread,pyqtSignal



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1407, 664)

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(f"background-image: url('image/tiao2.jpg');")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(1090, 180, 121, 41))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(1240, 180, 141, 41))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(1090, 240, 141, 41))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(1240, 240, 151, 51))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(1090, 70, 101, 31))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(1090, 300, 161, 41))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(1240, 70, 111, 31))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(1240, 300, 151, 51))
        self.radioButton_8.setObjectName("radioButton_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1090, 540, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(1250,540,101,41))
        self.pushButton_1.setObjectName(("pushButton_1"))
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(1090, 430, 191, 91))
        self.textEdit.setObjectName("textEdit")

        self.labelx = QtWidgets.QLabel(self.centralwidget)
        self.labelx.setGeometry(QtCore.QRect(600, 230, 461, 281))
        self.labelx.setObjectName("label")

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(680, 0, 711, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")



        self.label2 = QtWidgets.QLabel(MainWindow)
        self.label2.setGeometry(QtCore.QRect(10, 20, 393, 547))
        self.label2.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label2.setText("")
        self.label2.setObjectName("label")
        self.pix = QtGui.QPixmap("image/beijing2.jpg")
        self.label2.setPixmap(self.pix)
        self.label2.setStyleSheet("border: 2px solid blue")
        self.label2.setScaledContents(True)

        self.labeln = QtWidgets.QLabel(MainWindow)
        self.labeln.setGeometry(QtCore.QRect(403, 20, 161, 547))
        self.labeln.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.labeln.setText("")
        self.labeln.setObjectName("label")
        self.pix2 = QtGui.QPixmap("image/logo2.jpg")
        self.labeln.setPixmap(self.pix2)
        self.labeln.setStyleSheet("border: 2px solid blue")
        self.labeln.setScaledContents(True)

        self.labels = QtWidgets.QLabel(MainWindow)
        self.labels.setGeometry(QtCore.QRect(1100, 550, 20, 20))
        self.labels.setText("")
        self.labels.setObjectName("label")
        self.pixs = QtGui.QPixmap("image/power2.png")
        self.labels.setPixmap(self.pixs)
        self.labels.setScaledContents(True)

        self.labela = QtWidgets.QLabel(MainWindow)
        self.labela.setGeometry(QtCore.QRect(1090, 20, 40, 40))
        self.labela.setText("")
        self.labela.setObjectName("label")
        self.pixa = QtGui.QPixmap("image/sportingm.png")
        self.labela.setPixmap(self.pixa)
        self.labela.setScaledContents(True)

        self.labelq = QtWidgets.QLabel(MainWindow)
        self.labelq.setGeometry(QtCore.QRect(600, 410, 461, 200))
        self.labelq.setText("")
        self.labelq.setObjectName("label")
        self.pixq = QtGui.QPixmap("image/bottom4.jpg")
        self.labelq.setPixmap(self.pixq)

        self.labelr = QtWidgets.QLabel(MainWindow)
        self.labelr.setGeometry(QtCore.QRect(1260, 550, 20, 20))
        self.labelr.setText("")
        self.labelr.setObjectName("label")
        self.pixr = QtGui.QPixmap("image/logout.png")
        self.labelr.setPixmap(self.pixr)

        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(640, 10, 300, 300))
        self.loading.setStyleSheet("")
        self.loading.setText("")
        self.loading.setObjectName("loading")
        self.gif = QtGui.QMovie('image/hula.gif')
        self.loading.setMovie(self.gif)
        self.gif.start()

        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(10, 0, 671, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(0, 10, 16, 591))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9.setGeometry(QtCore.QRect(1090, 360, 141, 41))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setGeometry(QtCore.QRect(1240, 360, 151, 51))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_13 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_13.setGeometry(QtCore.QRect(1090, 120, 111, 41))
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_14 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_14.setGeometry(QtCore.QRect(1240, 120, 111, 41))
        self.radioButton_14.setObjectName("radioButton_14")

        self.labelj = QtWidgets.QLabel(self.centralwidget)
        self.labelj.setGeometry(QtCore.QRect(1130, 20, 161, 31))
        self.labelj.setObjectName("label")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 590, 1381, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1070, 10, 16, 591))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1380, 10, 20, 591))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(580, 10, 20, 591))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(1080, 410, 311, 16))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1407, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("image/1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(self.icon)

        self.radioButton_5.toggled.connect(self.select)
        self.radioButton_7.toggled.connect(self.select)
        self.radioButton_13.toggled.connect(self.select)
        self.radioButton_14.toggled.connect(self.select)
        self.radioButton.toggled.connect(self.select)
        self.radioButton_2.toggled.connect(self.select)
        self.radioButton_3.toggled.connect(self.select)
        self.radioButton_4.toggled.connect(self.select)
        self.radioButton_6.toggled.connect(self.select)
        self.radioButton_8.toggled.connect(self.select)
        self.radioButton_9.toggled.connect(self.select)
        self.radioButton_10.toggled.connect(self.select)

        self.pushButton_1.clicked.connect(self.exit)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智能运动计数系统"))
        self.radioButton.setText(_translate("MainWindow", "定时俯卧撑"))
        self.radioButton_2.setText(_translate("MainWindow", "定量俯卧撑"))
        self.radioButton_3.setText(_translate("MainWindow", "定时仰卧起坐"))
        self.radioButton_4.setText(_translate("MainWindow", "定量仰卧起坐"))
        self.radioButton_5.setText(_translate("MainWindow", "定时深蹲"))
        self.radioButton_6.setText(_translate("MainWindow", "定时引体向上"))
        self.radioButton_7.setText(_translate("MainWindow", "定量深蹲"))
        self.radioButton_8.setText(_translate("MainWindow", "定量引体向上"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.pushButton_1.setText(_translate("MainWindow","关闭"))
        self.textEdit.setPlaceholderText("请输入训练时间（个数） o(--)o")
        self.radioButton_9.setText(_translate("MainWindow", "定时卷腹运动"))
        self.radioButton_10.setText(_translate("MainWindow", "定量卷腹运动"))
        self.radioButton_13.setText(_translate("MainWindow", "定时跳绳"))
        self.radioButton_14.setText(_translate("MainWindow", "定量跳绳"))
        self.labelj.setText(_translate("MainWindow", "请选择训练类别"))
        self.labelx.setText(_translate("MainWindow","程序使用须知：\n"
                                                    "1.程序按钮为单选按钮选中后无法更改，\n如果选错请点击'关闭'按钮重启后打开\n"
                                                    "2.选择对应的训练类别并点击相应的按钮\n"
                                                    "3.填写相应的训练时间或者训练数量\n"
                                                    "4.在程序正式开始之前先跟着屏幕上的大象做热身运动吧"))

    def exit(self):
        app = QApplication.instance()
        app.quit()


    def select(self):
        if self.radioButton_13.isChecked():
            QMessageBox.information(MainWindow, "提示框", "欢迎您", QMessageBox.Yes)
            self.pushButton.clicked.connect(self.tiaoshi)
        elif self.radioButton_5.isChecked():
            self.pushButton.clicked.connect(self.shenshi)
        elif self.radioButton_7.isChecked():
            self.pushButton.clicked.connect(self.shenliang)
        elif self.radioButton_14.isChecked():
            self.pushButton.clicked.connect(self.tiaoliang)
        elif self.radioButton.isChecked():
            self.pushButton.clicked.connect(self.fushi)
        elif self.radioButton_2.isChecked():
            self.pushButton.clicked.connect(self.fuliang)
        elif self.radioButton_3.isChecked():
            self.pushButton.clicked.connect(self.yangshi)
        elif self.radioButton_4.isChecked():
            self.pushButton.clicked.connect(self.yangliang)
        elif self.radioButton_6.isChecked():
            self.pushButton.clicked.connect(self.yinshi)
        elif self.radioButton_8.isChecked():
            self.pushButton.clicked.connect(self.yinliang)
        elif self.radioButton_9.isChecked():
            self.pushButton.clicked.connect(self.juanshi)
        elif self.radioButton_10.isChecked():
            self.pushButton.clicked.connect(self.juanliang)



    def tiaoshi(self):
            #self.opengif()
            a = self.textEdit.toPlainText()
            import numpy as np
            import pyttsx3
            import time
            yuyin = pyttsx3.init()
            yuyin.say("欢迎您进行定时跳绳训练，程序加载较慢请耐心等待")
            yuyin.runAndWait()
            number = int(a)

            def get_points(results):
                count = 0
                num = 0
                all_num = []
                flip_list = []
                coords = np.array(results.pose_landmarks.landmark)

                # 汇总所有点的XYZ坐标
                def get_x(each):
                    return each.x

                def get_y(each):
                    return each.y

                def get_z(each):
                    return each.z

                    # 分别获取关键点XYZ坐标

                points_x = np.array(list(map(get_x, coords)))
                points_y = np.array(list(map(get_y, coords)))
                points_z = np.array(list(map(get_z, coords)))
                # 将三个方向坐标合并
                points = np.vstack((points_x, points_y, points_z)).T
                return points[0][1]


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

            def score_table(exercise, count, ret):
                score_table = cv2.imread("score_table.png")
                cv2.putText(score_table, "Activity : " + exercise,
                            (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                            cv2.LINE_AA)
                cv2.putText(score_table, "Counter : " + str(count), (10, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
                cv2.putText(score_table, "Status : " + str(ret), (10, 135),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
                cv2.imshow("Score Table", score_table)

            import cv2
            import time
            from matplotlib import pyplot as plt
            import numpy as np

            flag = False
            count = 0
            num = 0
            x = []
            y = []
            count_list = [0]

            # 调用摄像头，传入0表示获取系统默认摄像头
            cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            #print(0)
            # 打开cap
            cap.open(0)
            #print(1)
            fp = 1
            i = -1
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter('output.mp4', fourcc, 30, (640, 480))
            with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                while cap.isOpened():
                    # 获取画面
                    success, frame = cap.read()
                    if success:
                        if (fp == 1):
                            # time.sleep(interval)
                            print("跳绳，一组"f'{number}'"秒")
                            yuyin.say("跳绳，一组"f'{number}'"秒")
                            yuyin.runAndWait()
                            print('3,2,1,开始~')
                            yuyin.say('3,2,1,开始~')
                            yuyin.runAndWait()
                            start_time = time.time()
                            fp = 0
                            plt.ion()  # 开启interactive mode 成功的关键函数
                            fig1 = plt.figure(1)
                        else:
                            end_time = time.time()
                            During = int(end_time - start_time)
                            # print(end_time)
                            if end_time - start_time >= number:
                                cap.release()
                                cv2.destroyAllWindows()
                                break
                    else:
                        print('Error')
                        break
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
                        # print(num)
                        if len(y) < 2:
                            continue
                        pre_point = y[len(y) - 2]
                        if point > pre_point and point - pre_point >= 0.03:
                            flag = True
                        if point < pre_point and flag == True and pre_point - point >= 0.03:
                            count = count + 1
                            flag = False
                        else:
                            pass
                        QApplication.processEvents()
                    except:
                        pass
                        # 展示处理后的三通道图像
                    cv2.putText(frame, "Count: {}".format(str(count)), (450, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.0,
                                (0, 0, 0),
                                2)
                    out.write(frame)
                    # cv2.putText(frame, 'hi', (550, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), 2)
                    out.write(frame)
                    cv2.imshow('my_window', frame)
                    score_table("Skip", count, not flag)
                    plt.clf()  # 清空画布上的所有内容
                    plt.plot(x, y, '-b')
                    plt.show
                    if cv2.waitKey(1) in [ord('q'), 27]:
                        cap.release()
                        cv2.destroyAllWindows()
                        print("很遗憾您未能完成本次的跳绳计划，下次加油")
                        yuyin.say("很遗憾您未能完成本次的跳绳计划，下次加油")
                        yuyin.runAndWait()
                        break

                        # 关闭摄像头
                plt.close(fig1)
                cap.release()
                cv2.destroyAllWindows()
                if count == 0:
                    print('运动结束，放松一下吧~')
                    yuyin.say('运动结束，放松一下吧~')
                    yuyin.runAndWait()
                    print("您本次跳了"f'{count}'"个,用时"f'{During}'"秒，继续加油~")
                    yuyin.say("您本次跳了"f'{count}'"个,用时"f'{During}'"秒，继续加油")
                    yuyin.runAndWait()
                else:
                    velocity = int(60 / (During / count))
                    print('运动结束，放松一下吧~')
                    yuyin.say('运动结束，放松一下吧~')
                    yuyin.runAndWait()
                    print("您本次跳了"f'{count}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油~")
                    yuyin.say("您本次跳了"f'{count}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油")
                    yuyin.runAndWait()

    def tiaoliang(self):
        # self.opengif()
        a = self.textEdit.toPlainText()
        import numpy as np
        import pyttsx3
        import time
        yuyin = pyttsx3.init()
        yuyin.say("欢迎您进行定量跳绳训练，程序加载较慢请耐心等待")
        yuyin.runAndWait()
        number = int(a)

        def get_points(results):
            count = 0
            num = 0
            all_num = []
            flip_list = []
            coords = np.array(results.pose_landmarks.landmark)

            # 汇总所有点的XYZ坐标
            def get_x(each):
                return each.x

            def get_y(each):
                return each.y

            def get_z(each):
                return each.z

                # 分别获取关键点XYZ坐标

            points_x = np.array(list(map(get_x, coords)))
            points_y = np.array(list(map(get_y, coords)))
            points_z = np.array(list(map(get_z, coords)))
            # 将三个方向坐标合并
            points = np.vstack((points_x, points_y, points_z)).T
            return points[0][1]

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

        def score_table(exercise, count, ret):
            score_table = cv2.imread("score_table.png")
            cv2.putText(score_table, "Activity : " + exercise,
                        (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                        cv2.LINE_AA)
            cv2.putText(score_table, "Counter : " + str(count), (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.putText(score_table, "Status : " + str(ret), (10, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.imshow("Score Table", score_table)

        import cv2
        import time
        from matplotlib import pyplot as plt
        import numpy as np

        flag = False
        count = 0
        num = 0
        x = []
        y = []
        count_list = [0]

        # 调用摄像头，传入0表示获取系统默认摄像头
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # print(0)
        # 打开cap
        cap.open(0)
        # print(1)
        fp = 1
        i = -1
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 30, (640, 480))
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                # 获取画面
                success, frame = cap.read()
                if success:
                    if (fp == 1):
                        # time.sleep(interval)
                        print("跳绳，一组"f'{number}'"个")
                        yuyin.say("跳绳，一组"f'{number}'"个")
                        yuyin.runAndWait()
                        print('3,2,1,开始~')
                        yuyin.say('3,2,1,开始~')
                        yuyin.runAndWait()
                        start_time = time.time()
                        fp = 0
                        plt.ion()  # 开启interactive mode 成功的关键函数
                        fig1 = plt.figure(1)
                    else:
                        end_time = time.time()
                        During = int(end_time - start_time)
                        # print(end_time)
                        if count >= number:
                            cap.release()
                            cv2.destroyAllWindows()
                            break
                else:
                    print('Error')
                    break
                img_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                results = pose.process(img_RGB)
                h, w = frame.shape[0], frame.shape[1]
                try:
                    mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                    for i in range(33):

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
                    # print(num)
                    if len(y) < 2:
                        continue
                    pre_point = y[len(y) - 2]
                    if point > pre_point and point - pre_point >= 0.03:
                        flag = True
                    if point < pre_point and flag == True and pre_point - point >= 0.03:
                        count = count + 1
                        flag = False
                    else:
                        pass
                    QApplication.processEvents()
                except:
                    pass
                    # 展示处理后的三通道图像
                cv2.putText(frame, "Count: {}".format(str(count)), (450, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.0,
                            (0, 0, 0),
                            2)
                out.write(frame)
                # cv2.putText(frame, 'hi', (550, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), 2)
                out.write(frame)
                cv2.imshow('my_window', frame)
                score_table("Skip", count, not flag)
                plt.clf()  # 清空画布上的所有内容
                plt.plot(x, y, '-b')
                plt.show
                if cv2.waitKey(1) in [ord('q'), 27]:
                    cap.release()
                    cv2.destroyAllWindows()
                    print("很遗憾您未能完成本次的跳绳计划，下次加油")
                    yuyin.say("很遗憾您未能完成本次的跳绳计划，下次加油")
                    yuyin.runAndWait()
                    break

                    # 关闭摄像头
            plt.close(fig1)
            cap.release()
            cv2.destroyAllWindows()
            if count == 0:
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次跳了"f'{count}'"个,用时"f'{During}'"秒，继续加油~")
                yuyin.say("您本次跳了"f'{count}'"个,用时"f'{During}'"秒，继续加油")
                yuyin.runAndWait()
            else:
                velocity = int(60 / (During / count))
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次跳了"f'{count}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油~")
                yuyin.say("您本次跳了"f'{count}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油")
                yuyin.runAndWait()

    def juanshi(self):
        a = self.textEdit.toPlainText()
        import cv2
        import mediapipe as mp
        import numpy as np
        import pandas as pd
        from tqdm import tqdm
        import time
        import os
        import math

        # drawing your body
        mp_drawing = mp.solutions.drawing_utils

        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(static_image_mode=True,  # 是静态还是连续视频帧
                            model_complexity=2,  # 选择人体姿态关键点检测模型，0性能差但快，2性能好但慢，1介于两者之间
                            smooth_landmarks=True,  # 选择平滑关键点
                            enable_segmentation=True,  # 是否人体抠图
                            min_detection_confidence=0.5,  # 置信度阈值
                            min_tracking_confidence=0.5)  # 追踪阈值

        def calculate_angle(a, b, c):
            a = np.array(a)  # First
            b = np.array(b)  # Mid
            c = np.array(c)  # End

            radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
            angle = np.abs(radians * 180.0 / np.pi)

            if angle > 180.0:
                angle = 360 - angle

            return angle

        # return body part x,y value

        def detection_body_part(landmarks, body_part_name):
            return [landmarks[mp_pose.PoseLandmark[body_part_name].value].x,
                    landmarks[mp_pose.PoseLandmark[body_part_name].value].y]

        # In[22]:

        def detection_body_parts(landmarks):
            body_parts = pd.DataFrame(columns=["body_part", "x", "y"])

            for i, lndmrk in enumerate(mp_pose.PoseLandmark):
                lndmrk = str(lndmrk).split(".")[1]
                cord = detection_body_part(landmarks, lndmrk)
                body_parts.loc[i] = lndmrk, cord[0], cord[1]

            return body_parts

        # In[23]:

        """
        - LEFT_ARM
        - RIGHT_ARM
        - LEFT_LEG
        - RIGHT_LEG
        - NECK
        - BACK
        """
        import pyttsx3
        import time

        yuyin = pyttsx3.init()
        yuyin.say("欢迎您进行定时卷腹运动训练，程序加载较慢请耐心等待")
        yuyin.runAndWait()
        number = int(a)

        def calculate_body_part_angle(landmarks, body_part_name):
            if body_part_name == "LEFT":
                l_shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
                l_hip = detection_body_part(landmarks, "LEFT_HIP")
                l_knee = detection_body_part(landmarks, "LEFT_KNEE")
                return calculate_angle(l_shoulder, l_hip, l_knee)
            elif body_part_name == "RIGHT":
                r_shoulder = detection_body_part(landmarks, "RIGHT_SHOULDER")
                r_hip = detection_body_part(landmarks, "RIGHT_HIP")
                r_knee = detection_body_part(landmarks, "RIGHT_KNEE")
                return calculate_angle(r_shoulder, r_hip, r_knee)

        def score_table(exercise, count, ret):
            score_table = cv2.imread("score_table.png")
            cv2.putText(score_table, "Activity : " + exercise,
                        (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                        cv2.LINE_AA)
            cv2.putText(score_table, "Counter : " + str(count), (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.putText(score_table, "Status : " + str(ret), (10, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.imshow("Score Table", score_table)

        cap = cv2.VideoCapture(0)
        cap.open(0)
        counter = 0
        status = False
        fp = 1
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 13, (640, 480))

        ## Setup mediapipe instance

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                # frame = cv2.resize(frame, (720, 420))

                if ret:
                    if (fp == 1):

                        # time.sleep(interval)
                        print("卷腹运动，一组"f'{number}'"秒")
                        yuyin.say("卷腹运动，一组"f'{number}'"秒")
                        yuyin.runAndWait()
                        print('3,2,1,开始~')
                        yuyin.say('3,2,1,开始~')
                        yuyin.runAndWait()
                        start_time = time.time()
                        fp = 0

                    else:
                        # print(num)
                        # frame = cv2.flip(frame, 1)

                        end_time = time.time()
                        During = int(end_time - start_time)
                        # print(end_time)
                        if During >= number:
                            break

                if not ret:
                    print('Error')
                    break

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(240, 128, 128), thickness=3, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(100, 149, 237), thickness=2, circle_radius=2)
                                          )
                h, w = frame.shape[0], frame.shape[1]
                # Extract landmarks
                try:
                    for i in range(33):  # 遍历33个关键点
                        # 获取该关键点的三维坐标
                        cx = int(results.pose_landmarks.landmark[i].x * w)
                        cy = int(results.pose_landmarks.landmark[i].y * h)
                        cz = results.pose_landmarks.landmark[i].z
                        radius = 4
                        if i == 0:  # 鼻尖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [11, 12]:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (233, 155, 6), -1)
                        elif i in [23, 24]:  # 踝关节
                            img = cv2.circle(image, (cx, cy), radius, (1, 240, 255), -1)
                        elif i in [13, 14]:  # 胳膊肘
                            img = cv2.circle(image, (cx, cy), radius, (140, 47, 240), -1)
                        elif i in [25, 26]:  # 膝盖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [15, 16, 27, 28]:  # 手腕和脚腕
                            img = cv2.circle(image, (cx, cy), radius, (223, 155, 60), -1)
                        elif i in [17, 19, 21]:  # 左手
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        elif i in [18, 20, 22]:  # 右手
                            img = cv2.circle(image, (cx, cy), radius, (16, 144, 247), -1)
                        elif i in [27, 29, 31]:  # 左脚
                            img = cv2.circle(image, (cx, cy), radius, (29, 123, 243), -1)
                        elif i in [28, 30, 32]:  # 右脚
                            img = cv2.circle(image, (cx, cy), radius, (193, 182, 255), -1)
                        elif i in [9, 10]:  # 嘴
                            img = cv2.circle(image, (cx, cy), radius, (205, 235, 255), -1)
                        elif i in [1, 2, 3, 4, 5, 6, 7, 8]:  # 眼及脸颊
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        else:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (0, 255, 0), -1)
                    landmarks = results.pose_landmarks.landmark
                    # Calculate angles
                    left_angle = calculate_body_part_angle(landmarks, "LEFT")
                    right_angle = calculate_body_part_angle(landmarks, "RIGHT")
                    cv2.putText(image, "left_angle: {}".format(left_angle),
                                (15, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, "right_angle: {}".format(right_angle),
                                (15, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    avg_angle = (left_angle + right_angle) // 2
                    cv2.putText(image,
                                "crunch: {}".format(str(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].visibility)),
                                (440, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                    # print(avg_angle)
                    if status == 0:
                        if avg_angle < 125:
                            counter += 1
                            status = True
                            # print("crunch: ", counter)
                    else:
                        if avg_angle > 130:
                            status = False
                    cv2.putText(image, "Count: {}".format(str(counter)),
                                (440, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                except:
                    pass

                # Render detections
                out.write(image)
                cv2.imshow('my_window', image)
                score_table("Crunch", counter, status)

                if cv2.waitKey(1) in [ord('q'), 27]:
                    cap.release()
                    cv2.destroyAllWindows()
                    print("很遗憾您未能完成本次的卷腹运动计划，下次加油")
                    yuyin.say("很遗憾您未能完成本次的卷腹运动计划，下次加油")
                    yuyin.runAndWait()
                    break

        cap.release()
        cv2.destroyAllWindows()
        if counter == 0:
            print('运动结束，放松一下吧~')
            yuyin.say('运动结束，放松一下吧~')
            yuyin.runAndWait()
            print("您本次卷腹运动做了"f'{counter}'"个,用时"f'{During}'"秒，继续加油~")
            yuyin.say("您本次卷腹运动做了"f'{counter}'"个,用时"f'{During}'"秒，继续加油")
            yuyin.runAndWait()
        else:
            velocity = int(60 / (During / counter))
            print('运动结束，放松一下吧~')
            yuyin.say('运动结束，放松一下吧~')
            yuyin.runAndWait()
            print("您本次卷腹运动做了"f'{counter}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油~")
            yuyin.say("您本次卷腹运动做了"f'{counter}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油")
            yuyin.runAndWait()

    def juanliang(self):
        a = self.textEdit.toPlainText()
        import cv2
        import mediapipe as mp
        import numpy as np
        import pandas as pd
        from tqdm import tqdm
        import time
        import os
        import math

        # drawing your body
        mp_drawing = mp.solutions.drawing_utils

        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(static_image_mode=True,  # 是静态还是连续视频帧
                            model_complexity=2,  # 选择人体姿态关键点检测模型，0性能差但快，2性能好但慢，1介于两者之间
                            smooth_landmarks=True,  # 选择平滑关键点
                            enable_segmentation=True,  # 是否人体抠图
                            min_detection_confidence=0.5,  # 置信度阈值
                            min_tracking_confidence=0.5)  # 追踪阈值

        def calculate_angle(a, b, c):
            a = np.array(a)  # First
            b = np.array(b)  # Mid
            c = np.array(c)  # End

            radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
            angle = np.abs(radians * 180.0 / np.pi)

            if angle > 180.0:
                angle = 360 - angle

            return angle

        # return body part x,y value

        def detection_body_part(landmarks, body_part_name):
            return [landmarks[mp_pose.PoseLandmark[body_part_name].value].x,
                    landmarks[mp_pose.PoseLandmark[body_part_name].value].y]

        # In[22]:

        def detection_body_parts(landmarks):
            body_parts = pd.DataFrame(columns=["body_part", "x", "y"])

            for i, lndmrk in enumerate(mp_pose.PoseLandmark):
                lndmrk = str(lndmrk).split(".")[1]
                cord = detection_body_part(landmarks, lndmrk)
                body_parts.loc[i] = lndmrk, cord[0], cord[1]

            return body_parts

        # In[23]:

        """
        - LEFT_ARM
        - RIGHT_ARM
        - LEFT_LEG
        - RIGHT_LEG
        - NECK
        - BACK
        """
        import pyttsx3
        import time

        yuyin = pyttsx3.init()
        yuyin.say("欢迎您进行定量卷腹运动训练，程序加载较慢请耐心等待")
        yuyin.runAndWait()
        number = int(a)

        def calculate_body_part_angle(landmarks, body_part_name):
            if body_part_name == "LEFT":
                l_shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
                l_hip = detection_body_part(landmarks, "LEFT_HIP")
                l_knee = detection_body_part(landmarks, "LEFT_KNEE")
                return calculate_angle(l_shoulder, l_hip, l_knee)
            elif body_part_name == "RIGHT":
                r_shoulder = detection_body_part(landmarks, "RIGHT_SHOULDER")
                r_hip = detection_body_part(landmarks, "RIGHT_HIP")
                r_knee = detection_body_part(landmarks, "RIGHT_KNEE")
                return calculate_angle(r_shoulder, r_hip, r_knee)

        def score_table(exercise, count, ret):
            score_table = cv2.imread("score_table.png")
            cv2.putText(score_table, "Activity : " + exercise,
                        (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                        cv2.LINE_AA)
            cv2.putText(score_table, "Counter : " + str(count), (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.putText(score_table, "Status : " + str(ret), (10, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.imshow("Score Table", score_table)

        cap = cv2.VideoCapture(0)
        cap.open(0)
        counter = 0
        status = False
        fp = 1
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 13, (640, 480))

        ## Setup mediapipe instance

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                # frame = cv2.resize(frame, (720, 420))

                if ret:
                    if (fp == 1):

                        # time.sleep(interval)
                        print("卷腹运动，一组"f'{number}'"个")
                        yuyin.say("卷腹运动，一组"f'{number}'"个")
                        yuyin.runAndWait()
                        print('3,2,1,开始~')
                        yuyin.say('3,2,1,开始~')
                        yuyin.runAndWait()
                        start_time = time.time()
                        fp = 0

                    else:
                        # print(num)
                        # frame = cv2.flip(frame, 1)

                        end_time = time.time()
                        During = int(end_time - start_time)
                        # print(end_time)
                        if counter >= number:
                            break

                if not ret:
                    print('Error')
                    break

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(240, 128, 128), thickness=3, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(100, 149, 237), thickness=2, circle_radius=2)
                                          )
                h, w = frame.shape[0], frame.shape[1]
                # Extract landmarks
                try:
                    for i in range(33):  # 遍历33个关键点
                        # 获取该关键点的三维坐标
                        cx = int(results.pose_landmarks.landmark[i].x * w)
                        cy = int(results.pose_landmarks.landmark[i].y * h)
                        cz = results.pose_landmarks.landmark[i].z
                        radius = 4
                        if i == 0:  # 鼻尖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [11, 12]:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (233, 155, 6), -1)
                        elif i in [23, 24]:  # 踝关节
                            img = cv2.circle(image, (cx, cy), radius, (1, 240, 255), -1)
                        elif i in [13, 14]:  # 胳膊肘
                            img = cv2.circle(image, (cx, cy), radius, (140, 47, 240), -1)
                        elif i in [25, 26]:  # 膝盖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [15, 16, 27, 28]:  # 手腕和脚腕
                            img = cv2.circle(image, (cx, cy), radius, (223, 155, 60), -1)
                        elif i in [17, 19, 21]:  # 左手
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        elif i in [18, 20, 22]:  # 右手
                            img = cv2.circle(image, (cx, cy), radius, (16, 144, 247), -1)
                        elif i in [27, 29, 31]:  # 左脚
                            img = cv2.circle(image, (cx, cy), radius, (29, 123, 243), -1)
                        elif i in [28, 30, 32]:  # 右脚
                            img = cv2.circle(image, (cx, cy), radius, (193, 182, 255), -1)
                        elif i in [9, 10]:  # 嘴
                            img = cv2.circle(image, (cx, cy), radius, (205, 235, 255), -1)
                        elif i in [1, 2, 3, 4, 5, 6, 7, 8]:  # 眼及脸颊
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        else:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (0, 255, 0), -1)
                    landmarks = results.pose_landmarks.landmark
                    # Calculate angles
                    left_angle = calculate_body_part_angle(landmarks, "LEFT")
                    right_angle = calculate_body_part_angle(landmarks, "RIGHT")
                    cv2.putText(image, "left_angle: {}".format(left_angle),
                                (15, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, "right_angle: {}".format(right_angle),
                                (15, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    avg_angle = (left_angle + right_angle) // 2
                    cv2.putText(image,
                                "crunch: {}".format(str(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].visibility)),
                                (440, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                    # print(avg_angle)
                    if status == False:
                        if avg_angle < 125:
                            counter += 1
                            status = True
                            # print("crunch: ", counter)
                    else:
                        if avg_angle > 130:
                            status = False
                    cv2.putText(image, "Count: {}".format(str(counter)),
                                (440, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                except:
                    pass

                # Render detections
                out.write(image)
                cv2.imshow('my_window', image)
                score_table("Crunch", counter, status)

                if cv2.waitKey(1) in [ord('q'), 27]:
                    cap.release()
                    cv2.destroyAllWindows()
                    print("很遗憾您未能完成本次的卷腹运动计划，下次加油")
                    yuyin.say("很遗憾您未能完成本次的卷腹运动计划，下次加油")
                    yuyin.runAndWait()
                    break

        cap.release()
        cv2.destroyAllWindows()
        if counter == 0:
            print('运动结束，放松一下吧~')
            yuyin.say('运动结束，放松一下吧~')
            yuyin.runAndWait()
            print("您本次卷腹运动做了"f'{counter}'"个,用时"f'{During}'"秒，继续加油~")
            yuyin.say("您本次卷腹运动做了"f'{counter}'"个,用时"f'{During}'"秒，继续加油")
            yuyin.runAndWait()
        else:
            velocity = int(60 / (During / counter))
            print('运动结束，放松一下吧~')
            yuyin.say('运动结束，放松一下吧~')
            yuyin.runAndWait()
            print("您本次卷腹运动做了"f'{counter}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油~")
            yuyin.say("您本次卷腹运动做了"f'{counter}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油")
            yuyin.runAndWait()

    def shenshi(self):
        # self.opengif()
        a = self.textEdit.toPlainText()
        import numpy as np
        import pyttsx3
        import time
        yuyin = pyttsx3.init()
        yuyin.say("欢迎您进行定时深蹲训练，程序加载较慢请耐心等待")
        yuyin.runAndWait()
        number = int(a)

        def get_points(results):
            count = 0
            num = 0
            all_num = []
            flip_list = []
            coords = np.array(results.pose_landmarks.landmark)

            # 汇总所有点的XYZ坐标
            def get_x(each):
                return each.x

            def get_y(each):
                return each.y

            def get_z(each):
                return each.z

                # 分别获取关键点XYZ坐标

            points_x = np.array(list(map(get_x, coords)))
            points_y = np.array(list(map(get_y, coords)))
            points_z = np.array(list(map(get_z, coords)))
            # 将三个方向坐标合并
            points = np.vstack((points_x, points_y, points_z)).T
            return points[0][1]

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

        def score_table(exercise, count, ret):
            score_table = cv2.imread("score_table.png")
            cv2.putText(score_table, "Activity : " + exercise,
                        (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                        cv2.LINE_AA)
            cv2.putText(score_table, "Counter : " + str(count), (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.putText(score_table, "Status : " + str(ret), (10, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.imshow("Score Table", score_table)

        import cv2
        import time
        from matplotlib import pyplot as plt
        import numpy as np

        flag = False
        count = 0
        num = 0
        x = []
        y = []
        count_list = [0]

        # 调用摄像头，传入0表示获取系统默认摄像头
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # print(0)
        # 打开cap
        cap.open(0)
        # print(1)
        fp = 1
        i = -1
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 30, (640, 480))
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                # 获取画面
                success, frame = cap.read()
                if success:
                    if (fp == 1):
                        # time.sleep(interval)
                        print("原地深蹲，一组"f'{number}'"秒")
                        yuyin.say("原地深蹲，一组"f'{number}'"秒")
                        yuyin.runAndWait()
                        print('3,2,1,开始~')
                        yuyin.say('3,2,1,开始~')
                        yuyin.runAndWait()
                        start_time = time.time()
                        fp = 0
                        plt.ion()  # 开启interactive mode 成功的关键函数
                        fig1 = plt.figure(1)
                    else:
                        end_time = time.time()
                        During = int(end_time - start_time)
                        # print(end_time)
                        if During >= number:
                            cap.release()
                            cv2.destroyAllWindows()
                            break
                else:
                    print('Error')
                    break
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
                    # print(num)
                    if len(y) < 2:
                        continue
                    pre_point = y[len(y) - 2]
                    if point > pre_point and point - pre_point >= 0.05:
                        flag = True
                    if point < pre_point and flag == True and pre_point - point >= 0.05:
                        count = count + 1
                        flag = False
                    else:
                        pass
                    QApplication.processEvents()
                except:
                    pass
                    # 展示处理后的三通道图像
                cv2.putText(frame, "Count: {}".format(str(count)), (450, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.0,
                            (0, 0, 0),
                            2)
                out.write(frame)
                # cv2.putText(frame, 'hi', (550, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), 2)
                out.write(frame)
                cv2.imshow('my_window', frame)
                score_table("Squat", count, not flag)
                plt.clf()  # 清空画布上的所有内容
                plt.plot(x, y, '-b')
                plt.show
                if cv2.waitKey(1) in [ord('q'), 27]:
                    cap.release()
                    cv2.destroyAllWindows()
                    print("很遗憾您未能完成本次的深蹲运动计划，下次加油")
                    yuyin.say("很遗憾您未能完成本次的深蹲运动计划，下次加油")
                    yuyin.runAndWait()
                    break

                    # 关闭摄像头
            plt.close(fig1)
            cap.release()
            cv2.destroyAllWindows()
            if count == 0:
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次深蹲运动做了"f'{count}'"个,用时"f'{During}'"秒，继续加油~")
                yuyin.say("您本次深蹲运动做了"f'{count}'"个,用时"f'{During}'"秒，继续加油")
                yuyin.runAndWait()
            else:
                velocity = int(60 / (During / count))
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次深蹲运动做了"f'{count}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油~")
                yuyin.say("您本次深蹲运动做了"f'{count}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油")
                yuyin.runAndWait()


    def shenliang(self):
        # self.opengif()
        a = self.textEdit.toPlainText()
        import numpy as np
        import pyttsx3
        import time
        yuyin = pyttsx3.init()
        yuyin.say("欢迎您进行定量深蹲训练，程序加载较慢请耐心等待")
        yuyin.runAndWait()
        number = int(a)

        def get_points(results):
            count = 0
            num = 0
            all_num = []
            flip_list = []
            coords = np.array(results.pose_landmarks.landmark)

            # 汇总所有点的XYZ坐标
            def get_x(each):
                return each.x

            def get_y(each):
                return each.y

            def get_z(each):
                return each.z

                # 分别获取关键点XYZ坐标

            points_x = np.array(list(map(get_x, coords)))
            points_y = np.array(list(map(get_y, coords)))
            points_z = np.array(list(map(get_z, coords)))
            # 将三个方向坐标合并
            points = np.vstack((points_x, points_y, points_z)).T
            return points[0][1]

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

        def score_table(exercise, count, ret):
            score_table = cv2.imread("score_table.png")
            cv2.putText(score_table, "Activity : " + exercise,
                        (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                        cv2.LINE_AA)
            cv2.putText(score_table, "Counter : " + str(count), (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.putText(score_table, "Status : " + str(ret), (10, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.imshow("Score Table", score_table)

        import cv2
        import time
        from matplotlib import pyplot as plt
        import numpy as np

        flag = False
        count = 0
        num = 0
        x = []
        y = []
        count_list = [0]

        # 调用摄像头，传入0表示获取系统默认摄像头
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # print(0)
        # 打开cap
        cap.open(0)
        # print(1)
        fp = 1
        i = -1
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 30, (640, 480))
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                # 获取画面
                success, frame = cap.read()
                if success:
                    if (fp == 1):
                        # time.sleep(interval)
                        print("原地深蹲，一组"f'{number}'"个")
                        yuyin.say("原地深蹲，一组"f'{number}'"个")
                        yuyin.runAndWait()
                        print('3,2,1,开始~')
                        yuyin.say('3,2,1,开始~')
                        yuyin.runAndWait()
                        start_time = time.time()
                        fp = 0
                        plt.ion()  # 开启interactive mode 成功的关键函数
                        fig1 = plt.figure(1)
                    else:
                        end_time = time.time()
                        During = int(end_time - start_time)
                        # print(end_time)
                        if count >= number:
                            cap.release()
                            cv2.destroyAllWindows()
                            break
                else:
                    print('Error')
                    break
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
                    # print(num)
                    if len(y) < 2:
                        continue
                    pre_point = y[len(y) - 2]
                    if point > pre_point and point - pre_point >= 0.05:
                        flag = True
                    if point < pre_point and flag == True and pre_point - point >= 0.05:
                        count = count + 1
                        flag = False
                    else:
                        pass
                    QApplication.processEvents()
                except:
                    pass
                    # 展示处理后的三通道图像
                cv2.putText(frame, "Count: {}".format(str(count)), (450, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.0,
                            (0, 0, 0),
                            2)
                out.write(frame)
                # cv2.putText(frame, 'hi', (550, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), 2)
                out.write(frame)
                cv2.imshow('my_window', frame)
                score_table("Squat", count, not flag)
                plt.clf()  # 清空画布上的所有内容
                plt.plot(x, y, '-b')
                plt.show
                if cv2.waitKey(1) in [ord('q'), 27]:
                    cap.release()
                    cv2.destroyAllWindows()
                    print("很遗憾您未能完成本次的深蹲运动计划，下次加油")
                    yuyin.say("很遗憾您未能完成本次的深蹲运动计划，下次加油")
                    yuyin.runAndWait()
                    break

                    # 关闭摄像头
            plt.close(fig1)
            cap.release()
            cv2.destroyAllWindows()
            if count == 0:
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次深蹲运动做了"f'{count}'"个,用时"f'{During}'"秒，继续加油~")
                yuyin.say("您本次深蹲运动做了"f'{count}'"个,用时"f'{During}'"秒，继续加油")
                yuyin.runAndWait()
            else:
                velocity = int(60 / (During / count))
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次深蹲运动做了"f'{count}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油~")
                yuyin.say("您本次深蹲运动做了"f'{count}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油")
                yuyin.runAndWait()


    def yangshi(self):
        a = self.textEdit.toPlainText()
        import cv2
        import mediapipe as mp
        import numpy as np
        import pandas as pd
        from tqdm import tqdm
        import time
        import os
        import math

        # drawing your body
        mp_drawing = mp.solutions.drawing_utils

        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(static_image_mode=True,  # 是静态还是连续视频帧
                            model_complexity=2,  # 选择人体姿态关键点检测模型，0性能差但快，2性能好但慢，1介于两者之间
                            smooth_landmarks=True,  # 选择平滑关键点
                            enable_segmentation=True,  # 是否人体抠图
                            min_detection_confidence=0.5,  # 置信度阈值
                            min_tracking_confidence=0.5)  # 追踪阈值



        def calculate_angle(a, b, c):
            a = np.array(a)  # First
            b = np.array(b)  # Mid
            c = np.array(c)  # End

            radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
            angle = np.abs(radians * 180.0 / np.pi)

            if angle > 180.0:
                angle = 360 - angle

            return angle

        # return body part x,y value

        def detection_body_part(landmarks, body_part_name):
            return [landmarks[mp_pose.PoseLandmark[body_part_name].value].x,
                    landmarks[mp_pose.PoseLandmark[body_part_name].value].y]

        # In[22]:

        def detection_body_parts(landmarks):
            body_parts = pd.DataFrame(columns=["body_part", "x", "y"])

            for i, lndmrk in enumerate(mp_pose.PoseLandmark):
                lndmrk = str(lndmrk).split(".")[1]
                cord = detection_body_part(landmarks, lndmrk)
                body_parts.loc[i] = lndmrk, cord[0], cord[1]

            return body_parts

        # In[23]:

        """
        - LEFT_ARM
        - RIGHT_ARM
        - LEFT_LEG
        - RIGHT_LEG
        - NECK
        - BACK
        """
        import pyttsx3
        import time

        yuyin = pyttsx3.init()
        yuyin.say("欢迎您进行定时仰卧起坐训练，程序加载较慢请耐心等待")
        yuyin.runAndWait()
        number = int(a)

        def calculate_body_part_angle(landmarks, body_part_name):
            if body_part_name == "LEFT":
                l_shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
                l_hip = detection_body_part(landmarks, "LEFT_HIP")
                l_knee = detection_body_part(landmarks, "LEFT_KNEE")
                return calculate_angle(l_shoulder, l_hip, l_knee)
            elif body_part_name == "RIGHT":
                r_shoulder = detection_body_part(landmarks, "RIGHT_SHOULDER")
                r_hip = detection_body_part(landmarks, "RIGHT_HIP")
                r_knee = detection_body_part(landmarks, "RIGHT_KNEE")
                return calculate_angle(r_shoulder, r_hip, r_knee)

        def score_table(exercise, count, ret):
            score_table = cv2.imread("score_table.png")
            cv2.putText(score_table, "Activity : " + exercise,
                        (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                        cv2.LINE_AA)
            cv2.putText(score_table, "Counter : " + str(count), (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.putText(score_table, "Status : " + str(ret), (10, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.imshow("Score Table", score_table)

        # cap = cv2.VideoCapture("push-up.mp4")
        cap = cv2.VideoCapture(0)
        cap.open(0)
        counter = 0
        status = False
        fp = 1
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 13, (640, 480))
        ## Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                # frame = cv2.resize(frame, (720, 420))
                if ret:
                    if (fp == 1):
                        # time.sleep(interval)
                        print("仰卧起坐，一组"f'{number}'"秒")
                        yuyin.say("仰卧起坐，一组"f'{number}'"秒")
                        yuyin.runAndWait()
                        print('3,2,1,开始~')
                        yuyin.say('3,2,1,开始~')
                        yuyin.runAndWait()
                        start_time = time.time()
                        fp = 0
                    else:
                        # print(num)
                        # frame = cv2.flip(frame, 1)

                        end_time = time.time()
                        During = int(end_time - start_time)
                        # print(end_time)
                        if end_time - start_time >= number:
                            break
                if not ret:
                    print('Error')
                    break

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(240, 128, 128), thickness=3, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(100, 149, 237), thickness=2, circle_radius=2)
                                          )
                h, w = frame.shape[0], frame.shape[1]
                # Extract landmarks
                try:
                    for i in range(33):  # 遍历33个关键点
                        # 获取该关键点的三维坐标
                        cx = int(results.pose_landmarks.landmark[i].x * w)
                        cy = int(results.pose_landmarks.landmark[i].y * h)
                        cz = results.pose_landmarks.landmark[i].z
                        radius = 4
                        if i == 0:  # 鼻尖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [11, 12]:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (233, 155, 6), -1)
                        elif i in [23, 24]:  # 踝关节
                            img = cv2.circle(image, (cx, cy), radius, (1, 240, 255), -1)
                        elif i in [13, 14]:  # 胳膊肘
                            img = cv2.circle(image, (cx, cy), radius, (140, 47, 240), -1)
                        elif i in [25, 26]:  # 膝盖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [15, 16, 27, 28]:  # 手腕和脚腕
                            img = cv2.circle(image, (cx, cy), radius, (223, 155, 60), -1)
                        elif i in [17, 19, 21]:  # 左手
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        elif i in [18, 20, 22]:  # 右手
                            img = cv2.circle(image, (cx, cy), radius, (16, 144, 247), -1)
                        elif i in [27, 29, 31]:  # 左脚
                            img = cv2.circle(image, (cx, cy), radius, (29, 123, 243), -1)
                        elif i in [28, 30, 32]:  # 右脚
                            img = cv2.circle(image, (cx, cy), radius, (193, 182, 255), -1)
                        elif i in [9, 10]:  # 嘴
                            img = cv2.circle(image, (cx, cy), radius, (205, 235, 255), -1)
                        elif i in [1, 2, 3, 4, 5, 6, 7, 8]:  # 眼及脸颊
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        else:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (0, 255, 0), -1)
                    landmarks = results.pose_landmarks.landmark
                    # Calculate angles
                    left_angle = calculate_body_part_angle(landmarks, "LEFT")
                    right_angle = calculate_body_part_angle(landmarks, "RIGHT")
                    cv2.putText(image, "Left_angle: {}".format(left_angle),
                                (15, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, "Right_angle: {}".format(right_angle),
                                (15, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    avg_angle = (left_angle + right_angle) // 2
                    cv2.putText(image,
                                "Push Up: {}".format(str(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].visibility)),
                                (460, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)

                    if status == 0:
                        if avg_angle < 55:
                            counter += 1
                            status = True
                            # print("Push-up: ", counter)
                    else:
                        if avg_angle > 105:
                            status = False
                    cv2.putText(image, "Count: {}".format(str(counter)),
                                (460, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                except:

                    pass

                # Render detections
                out.write(image)
                cv2.imshow('my_window', image)
                score_table("Sit-up", counter, status)

                if cv2.waitKey(1) in [ord('q'), 27]:
                    cap.release()
                    cv2.destroyAllWindows()
                    print("很遗憾您未能完成本次的仰卧起坐计划，下次加油")
                    yuyin.say("很遗憾您未能完成本次的仰卧起坐计划，下次加油")
                    yuyin.runAndWait()
                    break

        cap.release()
        cv2.destroyAllWindows()
        if counter == 0:
            print('运动结束，放松一下吧~')
            yuyin.say('运动结束，放松一下吧~')
            yuyin.runAndWait()
            print("您本次做了"f'{counter}'"个,用时"f'{During}'"秒，继续加油~")
            yuyin.say("您本次做了"f'{counter}'"个,用时"f'{During}'"秒，继续加油")
            yuyin.runAndWait()
        else:
            velocity = int(60 / (During / counter))
            print('运动结束，放松一下吧~')
            yuyin.say('运动结束，放松一下吧~')
            yuyin.runAndWait()
            print("您本次做了"f'{counter}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油~")
            yuyin.say("您本次做了"f'{counter}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油")
            yuyin.runAndWait()


    def yangliang(self):
        a = self.textEdit.toPlainText()
        import cv2
        import mediapipe as mp
        import numpy as np
        import pandas as pd
        from tqdm import tqdm
        import time
        import os
        import math

        # drawing your body
        mp_drawing = mp.solutions.drawing_utils

        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(static_image_mode=True,  # 是静态还是连续视频帧
                            model_complexity=2,  # 选择人体姿态关键点检测模型，0性能差但快，2性能好但慢，1介于两者之间
                            smooth_landmarks=True,  # 选择平滑关键点
                            enable_segmentation=True,  # 是否人体抠图
                            min_detection_confidence=0.5,  # 置信度阈值
                            min_tracking_confidence=0.5)  # 追踪阈值



        def calculate_angle(a, b, c):
            a = np.array(a)  # First
            b = np.array(b)  # Mid
            c = np.array(c)  # End

            radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
            angle = np.abs(radians * 180.0 / np.pi)

            if angle > 180.0:
                angle = 360 - angle

            return angle

        # return body part x,y value

        def detection_body_part(landmarks, body_part_name):
            return [landmarks[mp_pose.PoseLandmark[body_part_name].value].x,
                    landmarks[mp_pose.PoseLandmark[body_part_name].value].y]

        # In[22]:

        def detection_body_parts(landmarks):
            body_parts = pd.DataFrame(columns=["body_part", "x", "y"])

            for i, lndmrk in enumerate(mp_pose.PoseLandmark):
                lndmrk = str(lndmrk).split(".")[1]
                cord = detection_body_part(landmarks, lndmrk)
                body_parts.loc[i] = lndmrk, cord[0], cord[1]

            return body_parts

        # In[23]:

        """
        - LEFT_ARM
        - RIGHT_ARM
        - LEFT_LEG
        - RIGHT_LEG
        - NECK
        - BACK
        """
        import pyttsx3
        import time

        yuyin = pyttsx3.init()
        yuyin.say("欢迎您进行定量仰卧起坐训练，程序加载较慢请耐心等待")
        yuyin.runAndWait()
        number = int(a)

        def calculate_body_part_angle(landmarks, body_part_name):
            if body_part_name == "LEFT":
                l_shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
                l_hip = detection_body_part(landmarks, "LEFT_HIP")
                l_knee = detection_body_part(landmarks, "LEFT_KNEE")
                return calculate_angle(l_shoulder, l_hip, l_knee)
            elif body_part_name == "RIGHT":
                r_shoulder = detection_body_part(landmarks, "RIGHT_SHOULDER")
                r_hip = detection_body_part(landmarks, "RIGHT_HIP")
                r_knee = detection_body_part(landmarks, "RIGHT_KNEE")
                return calculate_angle(r_shoulder, r_hip, r_knee)

        def score_table(exercise, count, ret):
            score_table = cv2.imread("score_table.png")
            cv2.putText(score_table, "Activity : " + exercise,
                        (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                        cv2.LINE_AA)
            cv2.putText(score_table, "Counter : " + str(count), (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.putText(score_table, "Status : " + str(ret), (10, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.imshow("Score Table", score_table)

        # cap = cv2.VideoCapture("push-up.mp4")
        cap = cv2.VideoCapture(0)
        cap.open(0)
        counter = 0
        status = False
        fp = 1
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 13, (640, 480))
        ## Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                # frame = cv2.resize(frame, (720, 420))
                if ret:
                    if (fp == 1):
                        # time.sleep(interval)
                        print("仰卧起坐，一组"f'{number}'"个")
                        yuyin.say("仰卧起坐，一组"f'{number}'"个")
                        yuyin.runAndWait()
                        print('3,2,1,开始~')
                        yuyin.say('3,2,1,开始~')
                        yuyin.runAndWait()
                        start_time = time.time()
                        fp = 0
                    else:
                        # print(num)
                        # frame = cv2.flip(frame, 1)

                        end_time = time.time()
                        During = int(end_time - start_time)
                        # print(end_time)
                        if counter >= number:
                            break
                if not ret:
                    print('Error')
                    break

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(240, 128, 128), thickness=3, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(100, 149, 237), thickness=2, circle_radius=2)
                                          )
                h, w = frame.shape[0], frame.shape[1]
                # Extract landmarks
                try:
                    for i in range(33):  # 遍历33个关键点
                        # 获取该关键点的三维坐标
                        cx = int(results.pose_landmarks.landmark[i].x * w)
                        cy = int(results.pose_landmarks.landmark[i].y * h)
                        cz = results.pose_landmarks.landmark[i].z
                        radius = 4
                        if i == 0:  # 鼻尖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [11, 12]:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (233, 155, 6), -1)
                        elif i in [23, 24]:  # 踝关节
                            img = cv2.circle(image, (cx, cy), radius, (1, 240, 255), -1)
                        elif i in [13, 14]:  # 胳膊肘
                            img = cv2.circle(image, (cx, cy), radius, (140, 47, 240), -1)
                        elif i in [25, 26]:  # 膝盖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [15, 16, 27, 28]:  # 手腕和脚腕
                            img = cv2.circle(image, (cx, cy), radius, (223, 155, 60), -1)
                        elif i in [17, 19, 21]:  # 左手
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        elif i in [18, 20, 22]:  # 右手
                            img = cv2.circle(image, (cx, cy), radius, (16, 144, 247), -1)
                        elif i in [27, 29, 31]:  # 左脚
                            img = cv2.circle(image, (cx, cy), radius, (29, 123, 243), -1)
                        elif i in [28, 30, 32]:  # 右脚
                            img = cv2.circle(image, (cx, cy), radius, (193, 182, 255), -1)
                        elif i in [9, 10]:  # 嘴
                            img = cv2.circle(image, (cx, cy), radius, (205, 235, 255), -1)
                        elif i in [1, 2, 3, 4, 5, 6, 7, 8]:  # 眼及脸颊
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        else:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (0, 255, 0), -1)
                    landmarks = results.pose_landmarks.landmark
                    # Calculate angles
                    left_angle = calculate_body_part_angle(landmarks, "LEFT")
                    right_angle = calculate_body_part_angle(landmarks, "RIGHT")
                    cv2.putText(image, "Left_angle: {}".format(left_angle),
                                (15, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, "Right_angle: {}".format(right_angle),
                                (15, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    avg_angle = (left_angle + right_angle) // 2
                    cv2.putText(image,
                                "Push Up: {}".format(str(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].visibility)),
                                (460, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)

                    if status == 0:
                        if avg_angle < 55:
                            counter += 1
                            status = True
                            # print("Push-up: ", counter)
                    else:
                        if avg_angle > 105:
                            status = False
                    cv2.putText(image, "Count: {}".format(str(counter)),
                                (460, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                except:

                    pass

                # Render detections
                out.write(image)
                cv2.imshow('my_window', image)
                score_table("Sit-up", counter, status)

                if cv2.waitKey(1) in [ord('q'), 27]:
                    cap.release()
                    cv2.destroyAllWindows()
                    print("很遗憾您未能完成本次的仰卧起坐计划，下次加油")
                    yuyin.say("很遗憾您未能完成本次的仰卧起坐计划，下次加油")
                    yuyin.runAndWait()
                    break

        cap.release()
        cv2.destroyAllWindows()
        if counter == 0:
            print('运动结束，放松一下吧~')
            yuyin.say('运动结束，放松一下吧~')
            yuyin.runAndWait()
            print("您本次做了"f'{counter}'"个,用时"f'{During}'"秒，继续加油~")
            yuyin.say("您本次做了"f'{counter}'"个,用时"f'{During}'"秒，继续加油")
            yuyin.runAndWait()
        else:
            velocity = int(60 / (During / counter))
            print('运动结束，放松一下吧~')
            yuyin.say('运动结束，放松一下吧~')
            yuyin.runAndWait()
            print("您本次做了"f'{counter}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油~")
            yuyin.say("您本次做了"f'{counter}'"个,用时"f'{During}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油")
            yuyin.runAndWait()

    def yinshi(self):
        a = self.textEdit.toPlainText()
        import cv2
        import mediapipe as mp
        import numpy as np
        import pandas as pd
        from tqdm import tqdm
        import time
        import os
        import math

        # drawing your body
        mp_drawing = mp.solutions.drawing_utils

        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(static_image_mode=True,  # 是静态还是连续视频帧
                            model_complexity=2,  # 选择人体姿态关键点检测模型，0性能差但快，2性能好但慢，1介于两者之间
                            smooth_landmarks=True,  # 选择平滑关键点
                            enable_segmentation=True,  # 是否人体抠图
                            min_detection_confidence=0.5,  # 置信度阈值
                            min_tracking_confidence=0.5)  # 追踪阈值

        def calculate_angle(a, b, c):
            a = np.array(a)  # First
            b = np.array(b)  # Mid
            c = np.array(c)  # End

            radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
            angle = np.abs(radians * 180.0 / np.pi)

            if angle > 180.0:
                angle = 360 - angle

            return angle

        def detection_body_part(landmarks, body_part_name):
            return [landmarks[mp_pose.PoseLandmark[body_part_name].value].x,
                    landmarks[mp_pose.PoseLandmark[body_part_name].value].y]

        def detection_body_parts(landmarks):
            body_parts = pd.DataFrame(columns=["body_part", "x", "y"])

            for i, lndmrk in enumerate(mp_pose.PoseLandmark):
                lndmrk = str(lndmrk).split(".")[1]
                cord = detection_body_part(landmarks, lndmrk)
                body_parts.loc[i] = lndmrk, cord[0], cord[1]

            return body_parts

        def score_table(exercise, count, ret):
            score_table = cv2.imread("score_table.png")
            cv2.putText(score_table, "Activity : " + exercise,
                        (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                        cv2.LINE_AA)
            cv2.putText(score_table, "Counter : " + str(count), (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.putText(score_table, "Status : " + str(ret), (10, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.imshow("Score Table", score_table)

        import pyttsx3
        import time

        yuyin = pyttsx3.init()
        yuyin.say("欢迎您进行定时引体向上训练，程序加载较慢请耐心等待")
        yuyin.runAndWait()
        number = int(a)

        def calculate_body_part_angle(landmarks, body_part_name):
            if body_part_name == "LEFT_ARM":
                l_shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
                l_elbow = detection_body_part(landmarks, "LEFT_ELBOW")
                l_wrist = detection_body_part(landmarks, "LEFT_WRIST")
                return calculate_angle(l_shoulder, l_elbow, l_wrist)

            elif body_part_name == "RIGHT_ARM":
                r_shoulder = detection_body_part(landmarks, "RIGHT_SHOULDER")
                r_elbow = detection_body_part(landmarks, "RIGHT_ELBOW")
                r_wrist = detection_body_part(landmarks, "RIGHT_WRIST")
                return calculate_angle(r_shoulder, r_elbow, r_wrist)

            elif body_part_name == "LEFT_LEG":
                l_hip = detection_body_part(landmarks, "LEFT_HIP")
                l_knee = detection_body_part(landmarks, "LEFT_KNEE")
                l_ankle = detection_body_part(landmarks, "LEFT_ANKLE")
                return calculate_angle(l_hip, l_knee, l_ankle)

            elif body_part_name == "RIGHT_LEG":
                r_hip = detection_body_part(landmarks, "RIGHT_HIP")
                r_knee = detection_body_part(landmarks, "RIGHT_KNEE")
                r_ankle = detection_body_part(landmarks, "RIGHT_ANKLE")
                return calculate_angle(r_hip, r_knee, r_ankle)

            elif body_part_name == "NECK":
                r_shoulder = detection_body_part(landmarks, "RIGHT_SHOULDER")
                l_shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
                r_mouth = detection_body_part(landmarks, "MOUTH_RIGHT")
                l_mouth = detection_body_part(landmarks, "MOUTH_LEFT")
                r_hip = detection_body_part(landmarks, "RIGHT_HIP")
                l_hip = detection_body_part(landmarks, "LEFT_HIP")

                shoulder_avg = [(r_shoulder[0] + l_shoulder[0]) / 2, (r_shoulder[1] + l_shoulder[1]) / 2]
                mouth_avg = [(r_mouth[0] + l_mouth[0]) / 2, (r_mouth[1] + l_mouth[1]) / 2]
                hip_avg = [(r_hip[0] + l_hip[0]) / 2, (r_hip[1] + l_hip[1]) / 2]

                return abs(180 - calculate_angle(mouth_avg, shoulder_avg, hip_avg))

        # In[27]:

        # cap = cv2.VideoCapture("push-up.mp4")
        cap = cv2.VideoCapture(0)
        cap.open(0)
        counter = 0
        status = False
        fp = 1
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 13, (640, 480))
        ## Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                # frame = cv2.resize(frame, (720, 420))
                if ret:
                    if (fp == 1):
                        # time.sleep(interval)
                        print("引体向上，一组"f'{number}'"秒")
                        yuyin.say("引体向上，一组"f'{number}'"秒")
                        yuyin.runAndWait()
                        print('3,2,1,开始~')
                        yuyin.say('3,2,1,开始~')
                        yuyin.runAndWait()
                        start_time = time.time()
                        fp = 0
                    else:
                        # print(num)
                        # frame = cv2.flip(frame, 1)

                        end_time = time.time()
                        during = int(end_time - start_time)
                        if during >= number:
                            cap.release()
                            cv2.destroyAllWindows()
                            break
                if not ret:
                    print('Error')
                    break

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(240, 128, 128), thickness=3, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(100, 149, 237), thickness=2, circle_radius=2)
                                          )
                h, w = frame.shape[0], frame.shape[1]
                # Extract landmarks
                try:
                    for i in range(33):  # 遍历33个关键点
                        # 获取该关键点的三维坐标
                        cx = int(results.pose_landmarks.landmark[i].x * w)
                        cy = int(results.pose_landmarks.landmark[i].y * h)
                        cz = results.pose_landmarks.landmark[i].z
                        radius = 4
                        if i == 0:  # 鼻尖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [11, 12]:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (233, 155, 6), -1)
                        elif i in [23, 24]:  # 踝关节
                            img = cv2.circle(image, (cx, cy), radius, (1, 240, 255), -1)
                        elif i in [13, 14]:  # 胳膊肘
                            img = cv2.circle(image, (cx, cy), radius, (140, 47, 240), -1)
                        elif i in [25, 26]:  # 膝盖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [15, 16, 27, 28]:  # 手腕和脚腕
                            img = cv2.circle(image, (cx, cy), radius, (223, 155, 60), -1)
                        elif i in [17, 19, 21]:  # 左手
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        elif i in [18, 20, 22]:  # 右手
                            img = cv2.circle(image, (cx, cy), radius, (16, 144, 247), -1)
                        elif i in [27, 29, 31]:  # 左脚
                            img = cv2.circle(image, (cx, cy), radius, (29, 123, 243), -1)
                        elif i in [28, 30, 32]:  # 右脚
                            img = cv2.circle(image, (cx, cy), radius, (193, 182, 255), -1)
                        elif i in [9, 10]:  # 嘴
                            img = cv2.circle(image, (cx, cy), radius, (205, 235, 255), -1)
                        elif i in [1, 2, 3, 4, 5, 6, 7, 8]:  # 眼及脸颊
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        else:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (0, 255, 0), -1)
                    landmarks = results.pose_landmarks.landmark
                    nose = detection_body_part(landmarks, "NOSE")
                    left_elbow = detection_body_part(landmarks, "LEFT_ELBOW")
                    right_elbow = detection_body_part(landmarks, "RIGHT_ELBOW")
                    avg_shoulder_y = (left_elbow[1] + right_elbow[1]) / 2

                    cv2.putText(image,
                                "Pull_Up: {}".format(str(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].visibility)),
                                (460, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                    cv2.putText(image, "Count: {}".format(str(counter)),
                                (460, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                    score_table("Pull-up", counter, status)
                    if status:
                        if nose[1] < avg_shoulder_y:
                            counter += 1
                            status = False
                    else:
                        if nose[1] > avg_shoulder_y:
                            status = True
                except:

                    pass

                # Render detections
                out.write(image)
                score_table("Push-up", counter, status)
                cv2.imshow('my_window', image)

                if cv2.waitKey(1) in [ord('q'), 27]:
                    cap.release()
                    cv2.destroyAllWindows()
                    print("很遗憾您未能完成本次的引体向上计划，下次加油")
                    yuyin.say("很遗憾您未能完成本次的引体向上计划，下次加油")
                    yuyin.runAndWait()
                    break
            if counter == 0:
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次引体向上运动做了"f'{counter}'"个,用时"f'{during}'"秒，继续加油~")
                yuyin.say("您本引体向上运动做了"f'{counter}'"个,用时"f'{during}'"秒，继续加油")
                yuyin.runAndWait()
            else:
                # 关闭摄像头
                velocity = int(60 / (during / counter))
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次引体向上运动做了"f'{counter}'"个,用时"f'{during}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油~")
                yuyin.say("您本次引体向上运动做了"f'{counter}'"个,用时"f'{during}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油")
                yuyin.runAndWait()

    def yinliang(self):
        a = self.textEdit.toPlainText()
        import cv2
        import mediapipe as mp
        # 获取坐标
        import numpy as np
        import pyttsx3
        import time
        import pandas as pd

        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(static_image_mode=True,  # 是静态还是连续视频帧
                            model_complexity=2,  # 选择人体姿态关键点检测模型，0性能差但快，2性能好但慢，1介于两者之间
                            smooth_landmarks=True,  # 选择平滑关键点
                            enable_segmentation=True,  # 是否人体抠图
                            min_detection_confidence=0.5,  # 置信度阈值
                            min_tracking_confidence=0.5)  # 追踪阈值

        def calculate_angle(a, b, c):
            a = np.array(a)  # First
            b = np.array(b)  # Mid
            c = np.array(c)  # End

            radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
            angle = np.abs(radians * 180.0 / np.pi)

            if angle > 180.0:
                angle = 360 - angle

            return angle

        def detection_body_part(landmarks, body_part_name):
            return [landmarks[mp_pose.PoseLandmark[body_part_name].value].x,
                    landmarks[mp_pose.PoseLandmark[body_part_name].value].y]

        def detection_body_parts(landmarks):
            body_parts = pd.DataFrame(columns=["body_part", "x", "y"])

            for i, lndmrk in enumerate(mp_pose.PoseLandmark):
                lndmrk = str(lndmrk).split(".")[1]
                cord = detection_body_part(landmarks, lndmrk)
                body_parts.loc[i] = lndmrk, cord[0], cord[1]

            return body_parts

        def score_table(exercise, count, ret):
            score_table = cv2.imread("score_table.png")
            cv2.putText(score_table, "Activity : " + exercise,
                        (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                        cv2.LINE_AA)
            cv2.putText(score_table, "Counter : " + str(count), (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.putText(score_table, "Status : " + str(ret), (10, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.imshow("Score Table", score_table)

        import pyttsx3
        import time

        yuyin = pyttsx3.init()
        yuyin.say("欢迎您进行定量引体向上训练，程序加载较慢请耐心等待")
        yuyin.runAndWait()
        number = int(a)

        def calculate_body_part_angle(landmarks, body_part_name):
            if body_part_name == "LEFT_ARM":
                l_shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
                l_elbow = detection_body_part(landmarks, "LEFT_ELBOW")
                l_wrist = detection_body_part(landmarks, "LEFT_WRIST")
                return calculate_angle(l_shoulder, l_elbow, l_wrist)

            elif body_part_name == "RIGHT_ARM":
                r_shoulder = detection_body_part(landmarks, "RIGHT_SHOULDER")
                r_elbow = detection_body_part(landmarks, "RIGHT_ELBOW")
                r_wrist = detection_body_part(landmarks, "RIGHT_WRIST")
                return calculate_angle(r_shoulder, r_elbow, r_wrist)

            elif body_part_name == "LEFT_LEG":
                l_hip = detection_body_part(landmarks, "LEFT_HIP")
                l_knee = detection_body_part(landmarks, "LEFT_KNEE")
                l_ankle = detection_body_part(landmarks, "LEFT_ANKLE")
                return calculate_angle(l_hip, l_knee, l_ankle)

            elif body_part_name == "RIGHT_LEG":
                r_hip = detection_body_part(landmarks, "RIGHT_HIP")
                r_knee = detection_body_part(landmarks, "RIGHT_KNEE")
                r_ankle = detection_body_part(landmarks, "RIGHT_ANKLE")
                return calculate_angle(r_hip, r_knee, r_ankle)

            elif body_part_name == "NECK":
                r_shoulder = detection_body_part(landmarks, "RIGHT_SHOULDER")
                l_shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
                r_mouth = detection_body_part(landmarks, "MOUTH_RIGHT")
                l_mouth = detection_body_part(landmarks, "MOUTH_LEFT")
                r_hip = detection_body_part(landmarks, "RIGHT_HIP")
                l_hip = detection_body_part(landmarks, "LEFT_HIP")

                shoulder_avg = [(r_shoulder[0] + l_shoulder[0]) / 2, (r_shoulder[1] + l_shoulder[1]) / 2]
                mouth_avg = [(r_mouth[0] + l_mouth[0]) / 2, (r_mouth[1] + l_mouth[1]) / 2]
                hip_avg = [(r_hip[0] + l_hip[0]) / 2, (r_hip[1] + l_hip[1]) / 2]

                return abs(180 - calculate_angle(mouth_avg, shoulder_avg, hip_avg))

        # In[27]:

        # cap = cv2.VideoCapture("push-up.mp4")
        cap = cv2.VideoCapture(0)
        cap.open(0)
        counter = 0
        status = False
        fp = 1
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 13, (640, 480))
        ## Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                # frame = cv2.resize(frame, (720, 420))
                if ret:
                    if (fp == 1):
                        # time.sleep(interval)
                        print("引体向上，一组"f'{number}'"个")
                        yuyin.say("引体向上，一组"f'{number}'"个")
                        yuyin.runAndWait()
                        print('3,2,1,开始~')
                        yuyin.say('3,2,1,开始~')
                        yuyin.runAndWait()
                        start_time = time.time()
                        fp = 0
                    else:
                        # print(num)
                        # frame = cv2.flip(frame, 1)
                        end_time = time.time()
                        during = int(end_time - start_time)
                if not ret:
                    print('Error')
                    break

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(240, 128, 128), thickness=3, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(100, 149, 237), thickness=2, circle_radius=2)
                                          )
                h, w = frame.shape[0], frame.shape[1]
                # Extract landmarks
                try:
                    for i in range(33):  # 遍历33个关键点
                        # 获取该关键点的三维坐标
                        cx = int(results.pose_landmarks.landmark[i].x * w)
                        cy = int(results.pose_landmarks.landmark[i].y * h)
                        cz = results.pose_landmarks.landmark[i].z
                        radius = 4
                        if i == 0:  # 鼻尖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [11, 12]:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (233, 155, 6), -1)
                        elif i in [23, 24]:  # 踝关节
                            img = cv2.circle(image, (cx, cy), radius, (1, 240, 255), -1)
                        elif i in [13, 14]:  # 胳膊肘
                            img = cv2.circle(image, (cx, cy), radius, (140, 47, 240), -1)
                        elif i in [25, 26]:  # 膝盖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [15, 16, 27, 28]:  # 手腕和脚腕
                            img = cv2.circle(image, (cx, cy), radius, (223, 155, 60), -1)
                        elif i in [17, 19, 21]:  # 左手
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        elif i in [18, 20, 22]:  # 右手
                            img = cv2.circle(image, (cx, cy), radius, (16, 144, 247), -1)
                        elif i in [27, 29, 31]:  # 左脚
                            img = cv2.circle(image, (cx, cy), radius, (29, 123, 243), -1)
                        elif i in [28, 30, 32]:  # 右脚
                            img = cv2.circle(image, (cx, cy), radius, (193, 182, 255), -1)
                        elif i in [9, 10]:  # 嘴
                            img = cv2.circle(image, (cx, cy), radius, (205, 235, 255), -1)
                        elif i in [1, 2, 3, 4, 5, 6, 7, 8]:  # 眼及脸颊
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        else:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (0, 255, 0), -1)
                    landmarks = results.pose_landmarks.landmark
                    # Calculate angles
                    '''
                    left_leg_angle = calculate_body_part_angle(landmarks, "LEFT_LEG")
                    right_leg_angle = calculate_body_part_angle(landmarks, "RIGHT_LEG")
                    left_arm_angle = calculate_body_part_angle(landmarks, "LEFT_ARM")
                    right_arm_angle = calculate_body_part_angle(landmarks, "RIGHT_ARM")
                    neck_angle = calculate_body_part_angle(landmarks, "NECK")
                    '''
                    nose = detection_body_part(landmarks, "NOSE")
                    left_elbow = detection_body_part(landmarks, "LEFT_ELBOW")
                    right_elbow = detection_body_part(landmarks, "RIGHT_ELBOW")
                    avg_shoulder_y = (left_elbow[1] + right_elbow[1]) / 2

                    cv2.putText(image,
                                "Pull_Up: {}".format(str(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].visibility)),
                                (460, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                    cv2.putText(image, "Count: {}".format(str(counter)),
                                (460, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                    score_table("Pull-up", counter, status)
                    if status:
                        if nose[1] < avg_shoulder_y:
                            counter += 1
                            status = False
                            if counter >= number:
                                cap.release()
                                cv2.destroyAllWindows()
                                break
                    else:
                        if nose[1] > avg_shoulder_y:
                            status = True
                except:
                    pass

                # Render detections
                out.write(image)
                cv2.imshow('my_window', image)
                if cv2.waitKey(1) in [ord('q'), 27]:
                    cap.release()
                    cv2.destroyAllWindows()
                    print("很遗憾您未能完成本次的引体向上计划，下次加油")
                    yuyin.say("很遗憾您未能完成本次的引体向上计划，下次加油")
                    yuyin.runAndWait()
                    break
            if counter == 0:
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次引体向上运动做了"f'{counter}'"个,用时"f'{during}'"秒，继续加油~")
                yuyin.say("您本次引体向上运动做了"f'{counter}'"个,用时"f'{during}'"秒，继续加油")
                yuyin.runAndWait()
            else:
                # 关闭摄像头
                velocity = int(60 / (during / counter))
                # 关闭图像窗口
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次引体向上运动做了"f'{counter}'"个,用时"f'{during}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油~")
                yuyin.say("您本次引体向上运动做了"f'{counter}'"个,用时"f'{during}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油")
                yuyin.runAndWait()

    def fushi(self):
        a = self.textEdit.toPlainText()
        import cv2
        import mediapipe as mp
        import numpy as np
        import pandas as pd
        from tqdm import tqdm
        import time
        import os
        import math

        # drawing your body
        mp_drawing = mp.solutions.drawing_utils

        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(static_image_mode=True,  # 是静态还是连续视频帧
                            model_complexity=2,  # 选择人体姿态关键点检测模型，0性能差但快，2性能好但慢，1介于两者之间
                            smooth_landmarks=True,  # 选择平滑关键点
                            enable_segmentation=True,  # 是否人体抠图
                            min_detection_confidence=0.5,  # 置信度阈值
                            min_tracking_confidence=0.5)  # 追踪阈值

        def calculate_angle(a, b, c):
            a = np.array(a)  # First
            b = np.array(b)  # Mid
            c = np.array(c)  # End

            radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
            angle = np.abs(radians * 180.0 / np.pi)

            if angle > 180.0:
                angle = 360 - angle

            return angle

        def detection_body_part(landmarks, body_part_name):
            return [landmarks[mp_pose.PoseLandmark[body_part_name].value].x,
                    landmarks[mp_pose.PoseLandmark[body_part_name].value].y]

        def detection_body_parts(landmarks):
            body_parts = pd.DataFrame(columns=["body_part", "x", "y"])

            for i, lndmrk in enumerate(mp_pose.PoseLandmark):
                lndmrk = str(lndmrk).split(".")[1]
                cord = detection_body_part(landmarks, lndmrk)
                body_parts.loc[i] = lndmrk, cord[0], cord[1]

            return body_parts

        def score_table(exercise, count, ret):
            score_table = cv2.imread("score_table.png")
            cv2.putText(score_table, "Activity : " + exercise,
                        (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                        cv2.LINE_AA)
            cv2.putText(score_table, "Counter : " + str(count), (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.putText(score_table, "Status : " + str(ret), (10, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.imshow("Score Table", score_table)

        import pyttsx3
        import time

        yuyin = pyttsx3.init()
        yuyin.say("欢迎您进行定时俯卧撑训练，程序加载较慢请耐心等待")
        yuyin.runAndWait()
        number = int(a)

        def calculate_body_part_angle(landmarks, body_part_name):
            if body_part_name == "LEFT_ARM":
                l_shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
                l_elbow = detection_body_part(landmarks, "LEFT_ELBOW")
                l_wrist = detection_body_part(landmarks, "LEFT_WRIST")
                return calculate_angle(l_shoulder, l_elbow, l_wrist)

            elif body_part_name == "RIGHT_ARM":
                r_shoulder = detection_body_part(landmarks, "RIGHT_SHOULDER")
                r_elbow = detection_body_part(landmarks, "RIGHT_ELBOW")
                r_wrist = detection_body_part(landmarks, "RIGHT_WRIST")
                return calculate_angle(r_shoulder, r_elbow, r_wrist)

            elif body_part_name == "LEFT_LEG":
                l_hip = detection_body_part(landmarks, "LEFT_HIP")
                l_knee = detection_body_part(landmarks, "LEFT_KNEE")
                l_ankle = detection_body_part(landmarks, "LEFT_ANKLE")
                return calculate_angle(l_hip, l_knee, l_ankle)

            elif body_part_name == "RIGHT_LEG":
                r_hip = detection_body_part(landmarks, "RIGHT_HIP")
                r_knee = detection_body_part(landmarks, "RIGHT_KNEE")
                r_ankle = detection_body_part(landmarks, "RIGHT_ANKLE")
                return calculate_angle(r_hip, r_knee, r_ankle)

            elif body_part_name == "NECK":
                r_shoulder = detection_body_part(landmarks, "RIGHT_SHOULDER")
                l_shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
                r_mouth = detection_body_part(landmarks, "MOUTH_RIGHT")
                l_mouth = detection_body_part(landmarks, "MOUTH_LEFT")
                r_hip = detection_body_part(landmarks, "RIGHT_HIP")
                l_hip = detection_body_part(landmarks, "LEFT_HIP")

                shoulder_avg = [(r_shoulder[0] + l_shoulder[0]) / 2, (r_shoulder[1] + l_shoulder[1]) / 2]
                mouth_avg = [(r_mouth[0] + l_mouth[0]) / 2, (r_mouth[1] + l_mouth[1]) / 2]
                hip_avg = [(r_hip[0] + l_hip[0]) / 2, (r_hip[1] + l_hip[1]) / 2]

                return abs(180 - calculate_angle(mouth_avg, shoulder_avg, hip_avg))

        # In[27]:

        # cap = cv2.VideoCapture("push-up.mp4")
        cap = cv2.VideoCapture(0)
        cap.open(0)
        counter = 0
        status = False
        fp = 1
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 13, (640, 480))
        ## Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                # frame = cv2.resize(frame, (720, 420))
                if ret:
                    if (fp == 1):
                        # time.sleep(interval)
                        print("俯卧撑，一组"f'{number}'"秒")
                        yuyin.say("俯卧撑，一组"f'{number}'"秒")
                        yuyin.runAndWait()
                        print('3,2,1,开始~')
                        yuyin.say('3,2,1,开始~')
                        yuyin.runAndWait()
                        start_time = time.time()
                        fp = 0
                    else:
                        # print(num)
                        # frame = cv2.flip(frame, 1)

                        end_time = time.time()
                        during = int(end_time - start_time)
                        if during >= number:
                            cap.release()
                            cv2.destroyAllWindows()
                            break
                if not ret:
                    print('Error')
                    break

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(240, 128, 128), thickness=3, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(100, 149, 237), thickness=2, circle_radius=2)
                                          )
                h, w = frame.shape[0], frame.shape[1]
                # Extract landmarks
                try:
                    for i in range(33):  # 遍历33个关键点
                        # 获取该关键点的三维坐标
                        cx = int(results.pose_landmarks.landmark[i].x * w)
                        cy = int(results.pose_landmarks.landmark[i].y * h)
                        cz = results.pose_landmarks.landmark[i].z
                        radius = 4
                        if i == 0:  # 鼻尖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [11, 12]:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (233, 155, 6), -1)
                        elif i in [23, 24]:  # 踝关节
                            img = cv2.circle(image, (cx, cy), radius, (1, 240, 255), -1)
                        elif i in [13, 14]:  # 胳膊肘
                            img = cv2.circle(image, (cx, cy), radius, (140, 47, 240), -1)
                        elif i in [25, 26]:  # 膝盖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [15, 16, 27, 28]:  # 手腕和脚腕
                            img = cv2.circle(image, (cx, cy), radius, (223, 155, 60), -1)
                        elif i in [17, 19, 21]:  # 左手
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        elif i in [18, 20, 22]:  # 右手
                            img = cv2.circle(image, (cx, cy), radius, (16, 144, 247), -1)
                        elif i in [27, 29, 31]:  # 左脚
                            img = cv2.circle(image, (cx, cy), radius, (29, 123, 243), -1)
                        elif i in [28, 30, 32]:  # 右脚
                            img = cv2.circle(image, (cx, cy), radius, (193, 182, 255), -1)
                        elif i in [9, 10]:  # 嘴
                            img = cv2.circle(image, (cx, cy), radius, (205, 235, 255), -1)
                        elif i in [1, 2, 3, 4, 5, 6, 7, 8]:  # 眼及脸颊
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        else:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (0, 255, 0), -1)
                    landmarks = results.pose_landmarks.landmark
                    # Calculate angles
                    left_leg_angle = calculate_body_part_angle(landmarks, "LEFT_LEG")
                    right_leg_angle = calculate_body_part_angle(landmarks, "RIGHT_LEG")
                    left_arm_angle = calculate_body_part_angle(landmarks, "LEFT_ARM")
                    right_arm_angle = calculate_body_part_angle(landmarks, "RIGHT_ARM")
                    neck_angle = calculate_body_part_angle(landmarks, "NECK")
                    cv2.putText(image, "Left Leg: {}".format(left_leg_angle),
                                (15, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, "Right Leg: {}".format(right_leg_angle),
                                (15, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, "Left Arm: {}".format(left_arm_angle),
                                (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, "Right Arm: {}".format(right_arm_angle),
                                (15, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, "Neck: {}".format(neck_angle),
                                (15, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    avg_arm_angle = (left_arm_angle + right_arm_angle) // 2
                    cv2.putText(image,
                                "Push Up: {}".format(str(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].visibility)),
                                (460, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)

                    if status == False:
                        if avg_arm_angle < 70:
                            counter += 1
                            status = True
                            # print("Push-up: ", counter)

                    else:
                        if avg_arm_angle > 160:
                            status = False
                    cv2.putText(image, "Count: {}".format(str(counter)),
                                (460, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                except:

                    pass

                # Render detections
                out.write(image)
                score_table("Push-up", counter, status)
                cv2.imshow('my_window', image)

                if cv2.waitKey(1) in [ord('q'), 27]:
                    cap.release()
                    cv2.destroyAllWindows()
                    print("很遗憾您未能完成本次的俯卧撑计划，下次加油")
                    yuyin.say("很遗憾您未能完成本次的俯卧撑计划，下次加油")
                    yuyin.runAndWait()
                    break
            if counter == 0:
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次俯卧撑运动做了"f'{counter}'"个,用时"f'{during}'"秒，继续加油~")
                yuyin.say("您本俯卧撑运动做了"f'{counter}'"个,用时"f'{during}'"秒，继续加油")
                yuyin.runAndWait()
            else:
                # 关闭摄像头
                velocity = int(60 / (during / counter))
                # 关闭图像窗口
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次俯卧撑运动做了"f'{counter}'"个,用时"f'{during}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油~")
                yuyin.say("您本次俯卧撑运动做了"f'{counter}'"个,用时"f'{during}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油")
                yuyin.runAndWait()

    def fuliang(self):
        a = self.textEdit.toPlainText()
        import cv2
        import mediapipe as mp
        # 获取坐标
        import numpy as np
        import pyttsx3
        import time
        import pandas as pd

        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose(static_image_mode=True,  # 是静态还是连续视频帧
                            model_complexity=2,  # 选择人体姿态关键点检测模型，0性能差但快，2性能好但慢，1介于两者之间
                            smooth_landmarks=True,  # 选择平滑关键点
                            enable_segmentation=True,  # 是否人体抠图
                            min_detection_confidence=0.5,  # 置信度阈值
                            min_tracking_confidence=0.5)  # 追踪阈值

        def calculate_angle(a, b, c):
            a = np.array(a)  # First
            b = np.array(b)  # Mid
            c = np.array(c)  # End

            radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
            angle = np.abs(radians * 180.0 / np.pi)

            if angle > 180.0:
                angle = 360 - angle

            return angle

        def detection_body_part(landmarks, body_part_name):
            return [landmarks[mp_pose.PoseLandmark[body_part_name].value].x,
                    landmarks[mp_pose.PoseLandmark[body_part_name].value].y]

        def detection_body_parts(landmarks):
            body_parts = pd.DataFrame(columns=["body_part", "x", "y"])

            for i, lndmrk in enumerate(mp_pose.PoseLandmark):
                lndmrk = str(lndmrk).split(".")[1]
                cord = detection_body_part(landmarks, lndmrk)
                body_parts.loc[i] = lndmrk, cord[0], cord[1]

            return body_parts

        def score_table(exercise, count, ret):
            score_table = cv2.imread("score_table.png")
            cv2.putText(score_table, "Activity : " + exercise,
                        (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2,
                        cv2.LINE_AA)
            cv2.putText(score_table, "Counter : " + str(count), (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.putText(score_table, "Status : " + str(ret), (10, 135),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (182, 158, 128), 2, cv2.LINE_AA)
            cv2.imshow("Score Table", score_table)

        import pyttsx3
        import time

        yuyin = pyttsx3.init()
        yuyin.say("欢迎您进行定量俯卧撑训练，程序加载较慢请耐心等待")
        yuyin.runAndWait()
        number = int(a)

        def calculate_body_part_angle(landmarks, body_part_name):
            if body_part_name == "LEFT_ARM":
                l_shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
                l_elbow = detection_body_part(landmarks, "LEFT_ELBOW")
                l_wrist = detection_body_part(landmarks, "LEFT_WRIST")
                return calculate_angle(l_shoulder, l_elbow, l_wrist)

            elif body_part_name == "RIGHT_ARM":
                r_shoulder = detection_body_part(landmarks, "RIGHT_SHOULDER")
                r_elbow = detection_body_part(landmarks, "RIGHT_ELBOW")
                r_wrist = detection_body_part(landmarks, "RIGHT_WRIST")
                return calculate_angle(r_shoulder, r_elbow, r_wrist)

            elif body_part_name == "LEFT_LEG":
                l_hip = detection_body_part(landmarks, "LEFT_HIP")
                l_knee = detection_body_part(landmarks, "LEFT_KNEE")
                l_ankle = detection_body_part(landmarks, "LEFT_ANKLE")
                return calculate_angle(l_hip, l_knee, l_ankle)

            elif body_part_name == "RIGHT_LEG":
                r_hip = detection_body_part(landmarks, "RIGHT_HIP")
                r_knee = detection_body_part(landmarks, "RIGHT_KNEE")
                r_ankle = detection_body_part(landmarks, "RIGHT_ANKLE")
                return calculate_angle(r_hip, r_knee, r_ankle)

            elif body_part_name == "NECK":
                r_shoulder = detection_body_part(landmarks, "RIGHT_SHOULDER")
                l_shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
                r_mouth = detection_body_part(landmarks, "MOUTH_RIGHT")
                l_mouth = detection_body_part(landmarks, "MOUTH_LEFT")
                r_hip = detection_body_part(landmarks, "RIGHT_HIP")
                l_hip = detection_body_part(landmarks, "LEFT_HIP")

                shoulder_avg = [(r_shoulder[0] + l_shoulder[0]) / 2, (r_shoulder[1] + l_shoulder[1]) / 2]
                mouth_avg = [(r_mouth[0] + l_mouth[0]) / 2, (r_mouth[1] + l_mouth[1]) / 2]
                hip_avg = [(r_hip[0] + l_hip[0]) / 2, (r_hip[1] + l_hip[1]) / 2]

                return abs(180 - calculate_angle(mouth_avg, shoulder_avg, hip_avg))

        # In[27]:

        # cap = cv2.VideoCapture("push-up.mp4")
        cap = cv2.VideoCapture(0)
        cap.open(0)
        counter = 0
        status = False
        fp = 1
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 13, (640, 480))
        ## Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                # frame = cv2.resize(frame, (720, 420))
                if ret:
                    if (fp == 1):
                        # time.sleep(interval)
                        print("俯卧撑，一组"f'{number}'"个")
                        yuyin.say("俯卧撑，一组"f'{number}'"个")
                        yuyin.runAndWait()
                        print('3,2,1,开始~')
                        yuyin.say('3,2,1,开始~')
                        yuyin.runAndWait()
                        start_time = time.time()
                        fp = 0
                    else:
                        # print(num)
                        # frame = cv2.flip(frame, 1)
                        end_time = time.time()
                        during = int(end_time - start_time)
                if not ret:
                    print('Error')
                    break

                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = pose.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(240, 128, 128), thickness=3, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(100, 149, 237), thickness=2, circle_radius=2)
                                          )
                h, w = frame.shape[0], frame.shape[1]
                # Extract landmarks
                try:
                    for i in range(33):  # 遍历33个关键点
                        # 获取该关键点的三维坐标
                        cx = int(results.pose_landmarks.landmark[i].x * w)
                        cy = int(results.pose_landmarks.landmark[i].y * h)
                        cz = results.pose_landmarks.landmark[i].z
                        radius = 4
                        if i == 0:  # 鼻尖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [11, 12]:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (233, 155, 6), -1)
                        elif i in [23, 24]:  # 踝关节
                            img = cv2.circle(image, (cx, cy), radius, (1, 240, 255), -1)
                        elif i in [13, 14]:  # 胳膊肘
                            img = cv2.circle(image, (cx, cy), radius, (140, 47, 240), -1)
                        elif i in [25, 26]:  # 膝盖
                            img = cv2.circle(image, (cx, cy), radius, (0, 0, 255), -1)
                        elif i in [15, 16, 27, 28]:  # 手腕和脚腕
                            img = cv2.circle(image, (cx, cy), radius, (223, 155, 60), -1)
                        elif i in [17, 19, 21]:  # 左手
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        elif i in [18, 20, 22]:  # 右手
                            img = cv2.circle(image, (cx, cy), radius, (16, 144, 247), -1)
                        elif i in [27, 29, 31]:  # 左脚
                            img = cv2.circle(image, (cx, cy), radius, (29, 123, 243), -1)
                        elif i in [28, 30, 32]:  # 右脚
                            img = cv2.circle(image, (cx, cy), radius, (193, 182, 255), -1)
                        elif i in [9, 10]:  # 嘴
                            img = cv2.circle(image, (cx, cy), radius, (205, 235, 255), -1)
                        elif i in [1, 2, 3, 4, 5, 6, 7, 8]:  # 眼及脸颊
                            img = cv2.circle(image, (cx, cy), radius, (94, 218, 121), -1)
                        else:  # 肩膀
                            img = cv2.circle(image, (cx, cy), radius, (0, 255, 0), -1)
                    landmarks = results.pose_landmarks.landmark
                    # Calculate angles
                    left_leg_angle = calculate_body_part_angle(landmarks, "LEFT_LEG")
                    right_leg_angle = calculate_body_part_angle(landmarks, "RIGHT_LEG")
                    left_arm_angle = calculate_body_part_angle(landmarks, "LEFT_ARM")
                    right_arm_angle = calculate_body_part_angle(landmarks, "RIGHT_ARM")
                    neck_angle = calculate_body_part_angle(landmarks, "NECK")
                    cv2.putText(image, "Left Leg: {}".format(left_leg_angle),
                                (15, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, "Right Leg: {}".format(right_leg_angle),
                                (15, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, "Left Arm: {}".format(left_arm_angle),
                                (15, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, "Right Arm: {}".format(right_arm_angle),
                                (15, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, "Neck: {}".format(neck_angle),
                                (15, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                (255, 255, 255), 2, cv2.LINE_AA)
                    avg_arm_angle = (left_arm_angle + right_arm_angle) // 2
                    cv2.putText(image,
                                "Push Up: {}".format(str(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].visibility)),
                                (460, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                    cv2.putText(image, "Count: {}".format(str(counter)),
                                (460, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                                (100, 149, 237), 2, cv2.LINE_AA)
                    score_table("Push-up", counter, status)
                    if status == 0:
                        if avg_arm_angle < 70:
                            counter += 1
                            status = True
                            # print("Push-up: ", counter)
                            if counter >= number:
                                during = int(end_time - start_time)
                                cap.release()
                                cv2.destroyAllWindows()
                                break

                    else:
                        if avg_arm_angle > 160:
                            status = False

                except:
                    pass

                # Render detections
                out.write(image)
                cv2.imshow('my_window', image)
                if cv2.waitKey(1) in [ord('q'), 27]:
                    cap.release()
                    cv2.destroyAllWindows()
                    print("很遗憾您未能完成本次的俯卧撑计划，下次加油")
                    yuyin.say("很遗憾您未能完成本次的俯卧撑计划，下次加油")
                    yuyin.runAndWait()
                    break
            if counter == 0:
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次俯卧撑运动做了"f'{counter}'"个,用时"f'{during}'"秒，继续加油~")
                yuyin.say("您本次俯卧撑运动做了"f'{counter}'"个,用时"f'{during}'"秒，继续加油")
                yuyin.runAndWait()
            else:
                # 关闭摄像头
                velocity = int(60 / (during / counter))
                print('运动结束，放松一下吧~')
                yuyin.say('运动结束，放松一下吧~')
                yuyin.runAndWait()
                print("您本次俯卧撑运动做了"f'{counter}'"个,用时"f'{during}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油~")
                yuyin.say("您本次俯卧撑运动做了"f'{counter}'"个,用时"f'{during}'"秒，平均速度为一分钟"f'{velocity}'"个,继续加油")
                yuyin.runAndWait()


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    mainwindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.setWindowFlags(QtCore.Qt.Dialog)
    mainwindow.show()
    sys.exit(app.exec_())