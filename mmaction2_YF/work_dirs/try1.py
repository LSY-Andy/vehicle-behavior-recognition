
import torch
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
from mmaction.apis import inference_recognizer, init_recognizer

# 初始化模型
config_file = 'configs/recognition/slowfast/finetune_ucf101_slowfast_r50_4x16x1_256e_kinetics400_rgb.py'
checkpoint_file = 'checkpoints/Something-Something-v2/SLOWFAST_8x8_R50.pkl'

device = 'cuda:0'  # 使用GPU加速
model = init_recognizer(config_file, checkpoint_file, device=device)

# 定义图像预处理管道
transform = Compose([
    Resize((256, 256)),
    CenterCrop((256, 256)),
    ToTensor(),
    Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# 加载图像
frames = [...]  # 每个元素是一帧图像
input_data = dict(
    imgs=frames,  # 图像帧列表
    modality='rgb',  # 使用RGB图像
    filename_tmpl='img_{:05}.jpg',  # 图像文件名模板
    start_index=1)  # 图像文件名中序号的起始值

# 预处理图像
for i, frame in enumerate(frames):
    frames[i] = transform(frame)
input_tensor = torch.stack(frames, dim=0)

# 进行模型推理
result = inference_recognizer(model, input_data)

# 输出模型预测结果
print(result)


