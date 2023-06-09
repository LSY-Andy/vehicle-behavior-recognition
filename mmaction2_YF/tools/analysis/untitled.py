
import json
import matplotlib.pyplot as plt

# 读取JSON文件
with open('/home/mmaction2_YF/20230516_203350.log.json', 'r') as file:
    data = json.load(file)

# 提取mAP值
mAP_values = [entry['mAP@0.5IOU'] for entry in data if 'mAP@0.5IOU' in entry]

# 创建x轴和y轴数据
epochs = range(1, len(mAP_values) + 1)
mAP_scores = [float(value) for value in mAP_values]

# 绘制折线图
plt.plot(epochs, mAP_scores, marker='o')
plt.xlabel('Epoch')
plt.ylabel('mAP@0.5IOU')
plt.title('mAP Progression')
plt.grid(True)

# 保存为PDF文件
plt.savefig('mAP_plot.pdf')

