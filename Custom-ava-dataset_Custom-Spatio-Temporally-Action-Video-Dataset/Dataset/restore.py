import csv
 
train_temp_path = './train_temp.csv'
# train_temp = [62]
train_temp = [86]
#这里只是定义了一个列表，只有一个元素为62


try:
    with open(train_temp_path) as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        for row in csv_reader:           
            train_temp.append(row)
# .append是在列表末尾添加一个元素，类似与[1,2,3].append(4)
# 在这里 就是将excel表的每一行添加到train_temp最后
# train_temp是一个二维数组，在这个数组中，每个元素是csv的一行的每个字段
except FileNotFoundError:
    print("The file train_temp.csv does not exist.")
    exit()
    
def update_train_temp(videoName,index,maxId):
    for index2 in range(len(train_temp)):
#         从第一行开始遍历，最开始data是第一行数据，后面data[0]就是第一行第一列
        data = train_temp[index2]
        if index2 < index:
            continue
        if videoName == data[0]:
            if index2 == index:
                train_temp[index][-1] = maxId + 1
                # 并且查查ava_train_temp[index]后面10个的坐标是否与ava_train_temp[index]一致
                # 如果一致，就让该ava_train_temp[index + n]的ID与ava_train_temp[index]一致
                x1 = float(train_temp[index][2])
                y1 = float(train_temp[index][3])
                x2 = float(train_temp[index][4])
                y2 = float(train_temp[index][5])
                # for index3 in range(10):
                for index3 in range((len(train_temp) - 1) - index):
                    if train_temp[index+index3+1][-1] == '-1':
                        xT1 = float(train_temp[index+index3+1][2])
                        yT1 = float(train_temp[index+index3+1][3])
                        xT2 = float(train_temp[index+index3+1][4])
                        yT2 = float(train_temp[index+index3+1][5])
                        if abs(x1-xT1)<0.005 and abs(y1-yT1)<0.005 and abs(x2-xT2)<0.005 and abs(y2-yT2)<0.005:
                            train_temp[index+index3+1][-1] = maxId + 1
                        else:
                            break
                    else:
                        break
                
                xTT1 = float(train_temp[index2][2])
                yTT1 = float(train_temp[index2][3])
                xTT2 = float(train_temp[index2][4])
                yTT2 = float(train_temp[index2][5])
                if abs(x1-xTT1)<0.005 and abs(y1-yTT1)<0.005 and abs(x2-xTT2)<0.005 and abs(y2-yTT2)<0.005:
                    continue
                train_temp[index2][-1] = int(train_temp[index2][-1]) + 1
        
        
                
temp = train_temp

# dicts存放修正后的ava_train_temp
dicts = []
# personID_indindexex 用来记录修正进行到的位置
personID_index = 0
# maxId用来记录当前视频的进行中最大的ID
maxId = -1
# videoName 用来记录当前视频的名字
videoName = ''


for index in range(len(temp)):
    data = temp[index]
    # 判断是否切换视频，如果切换视频，
    # 那么videoName改变、maxId重制

    if videoName!=data[0]:
        videoName = data[0]
        maxId = -1
    # videoName = data[0]
    
    if maxId < int(data[-1]):
        maxId = int(data[-1])

    if data[-1] == '-1':
        update_train_temp(videoName,index,maxId)
        # 经过 update_ava_train_temp 后，data[-1]为‘-1’对应的坐标的ID赋予maxID+1，那么最高值也要+1
        maxId = maxId + 1
    

# for index in range(len(train_temp)):
#     # 判断是否切换视频，如果切换视频，
#     # 那么videoName改变、maxId重制

#     if videoName!=data[0]:
#         videoName = data[0]
#         maxId = -1
    
#     if maxId < int(data[-1]):
#         maxId = int(data[-1])

#     if data[-1] == '-1':
#         update_train_temp(videoName,index,maxId)
#         # 经过 update_ava_train_temp 后，data[-1]为‘-1’对应的坐标的ID赋予maxID+1，那么最高值也要+1
#         maxId = maxId + 1
        
with open('./annotations/train.csv',"w") as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerows(train_temp)
   