import torch
from torchvision.transforms import Compose,Resize,CenterCrop,ToTensor,Normalize
from slowfast.models import SlowFast
from slowfast.utils.checkpoint import load_checkpoint

model=SlowFast()
load_checkpoint("/home/mmaction2_YF/work_dirs/ava/slowfast_kinetics_pretrained_r50_4x16x1_20e_ava_rgb/best_mAP@0.5IOU_epoch_18.pth",model)

transform = Compose({
    Resize((256,256)),
    CenterCrop((256,256)),
    ToTensor(),
    Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
    })

image = Image.open(Custom-ava-dataset_Custom-Spatio-Temporally-Action-Video-Dataset/Dataset/choose_frames_all/1_000001.jpg)

input_tensor = transform(image).unsqueeze(0)

with torch.no_grad():
    model.eval()
    output = model(input_tensor)


print(output)
