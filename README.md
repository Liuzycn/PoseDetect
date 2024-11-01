# PoseDetect

## Project Significance
With the improvement of people's living standards, especially since the pandemic, there has been a growing emphasis on physical exercise. However, it is often challenging for individuals to assess their workout intensity accurately. Our project aims to assist users by counting repetitions and measuring the rate during exercises such as push-ups, sit-ups, and more. After a workout, users can clearly see their exercise volume, providing them with a better understanding of their physical activity.

Additionally, users can control their workout volume by setting goals based on time or repetition count, allowing them to maximize their workout efficiency.

Our project is capable of counting multiple exercise postures (e.g., push-ups, sit-ups, etc.), not just a single type of exercise. This flexibility meets users' diverse workout needs, supporting a variety of exercise routines.

## Project Content

### First Part
Environment Setup: Installation of the OpenPose model (an open-source library developed by Carnegie Mellon University based on convolutional neural networks and supervised learning, using Caffe as the framework, capable of estimating human poses, facial expressions, and finger movements). Setting up and configuring the PyQt5 environment.

### Second Part
Human Keypoint Detection: Using the camera feed, the OpenPose model is called to detect human keypoints, connecting key points to form an entire skeletal structure.

Figure 1: Keypoint Detection

### Third Part
Counting Functionality: The camera continuously detects frames in real-time to calculate changes in human keypoints, displaying the exercise name, count, and status in the workout window to track repetitions. It provides real-time angle detection for push-ups and displays fluctuation graphs of coordinate changes for squats and jump rope. There is voice guidance throughout the exercise, assisting users as they work out.

Figure 2: Display of Counting Process

### Fourth Part
Program Development: Using PyQt5 to design the user interface, which includes background images, animations, and instructional text for an aesthetically pleasing display. Users can select the exercise they wish to perform. The interface offers timed and quantified training for 12 types of exercises (jump rope, squats, sit-ups, push-ups, pull-ups, crunches, etc.).

