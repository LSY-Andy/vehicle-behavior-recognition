import csv

train_temp_path = './train_temp.csv'
train_temp = []

try:
    with open(train_temp_path) as csvfile:
        csv_reader = csv.reader(csvfile)  
        for row in csv_reader:           
            train_temp.append(row)
except FileNotFoundError:
    print("The file train_temp.csv does not exist.")
    exit()

def update_train_temp(videoName,index,maxId):
    for index2 in range(len(train_temp)):
        data = train_temp[index2]
        if index2 < index:
            continue
        if videoName == data[0]:
            if index2 == index:
                train_temp[index][-1] = maxId + 1
                x1 = float(train_temp[index][2])
                y1 = float(train_temp[index][3])
                x2 = float(train_temp[index][4])
                y2 = float(train_temp[index][5])
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
            else:
                if train_temp[index2][-1] == '-1':
                    continue
                if type(train_temp[index2][-1]) == int: 
                    maxId = int(maxId)
                elif type(train_temp[index2][-1]) == str:
                    maxId = int(maxId)
                if maxId < int(train_temp[index2][-1]):
                    maxId = int(train_temp[index2][-1])
                
temp = train_temp

dicts = []
personID_index = 0
maxId = -1
videoName = ''

for index in range(len(temp)):
    data = []
    data = temp[index]
    if videoName!=data[0]:
        videoName = data[0]
        maxId = -1
    if type(data[-1]) == int: 
        maxId = int(maxId)
    elif type(data[-1]) == str:
        maxId = int(maxId)