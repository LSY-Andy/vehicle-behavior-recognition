import cv2
import torch
import numpy as np
from mmcv import Config
from mmaction.apis import init_recognizer, inference_recognizer

# 加载模型配置文件和权重文件
cfg_file = '/home/mmaction2_YF/configs/detection/ava/my_slowfast_kinetics_pretrained_r50_4x16x1_20e_ava_rgb.py'
checkpoint_file = '/home/mmaction2_YF/work_dirs/ava/slowfast_kinetics_pretrained_r50_4x16x1_20e_ava_rgb/best_mAP@0.5IOU_epoch_11.pth'
cfg = Config.fromfile(cfg_file)

# 初始化模型
model = init_recognizer(cfg, checkpoint_file, device='cuda:0')
model.cfg = cfg

# 打开网络摄像头
cap = cv2.VideoCapture(0)

# 循环读取摄像头数据并进行推理
while True:
    # 读取一帧图像
    ret, frame = cap.read()
   
    # 将图像转换为模型所需格式
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img.astype(np.float32) / 255.
    img = img.transpose(2, 0, 1)[np.newaxis, :]
    input_data = dict(
        imgs=img,
        img_shape=(224, 224),
        modality='RGB',
        filename_tmpl='img_{:05}.jpg')
   
    # 进行模型推理
    with torch.no_grad():
        result = inference_recognizer(model, **input_data)
   
    # 可以根据预测结果对视频进行可视化或后处理
    print(result)
   
    # 显示结果
    cv2.imshow('result', frame)
   
    # 按下q键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()



 
