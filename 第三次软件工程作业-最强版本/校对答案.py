import pandas as pd
import numpy as np
import argparse

def get_Parameter():#命令行控制模块
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', help='题目', type=str)
    parser.add_argument('-a', help='题目的答案', type=str)
    return parser.parse_args()

args = get_Parameter()
e = args.e
a = args.a



def text_save(filename, data):#filename为写入文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    file.seek(0)
    file.truncate() # 清空文件
    for x in data:
        x='%s\n'%(x)
        file.write(x)
    file.close()
    print('%s文件保存成功'%filename)

Answers = pd.read_csv('Answers_list.csv')

Answers_list = np.array(Answers)
f = open('test.txt', 'r', encoding='utf-8')
data_lists = f.readlines()	#读出的是str类
dataset= []
# 对每一行作循环
for data in data_lists:
    data1 = data.strip('\n')	# 去掉开头和结尾的换行符
    data2 = data1.split('\t')	# 把tab作为间隔符
    dataset.append(data2)	# 把这一行的结果作为元素加入列表datase
dataset = np.array(dataset)
correct_list = []
wrong_list = []

for i in range(len(Answers_list)):
    if Answers_list[i] == dataset[i]:
        correct_list.append(i+1)
    else:
        wrong_list.append(i+1)
print('Correct:', len(correct_list), correct_list)
print('Wrong:', len(wrong_list), wrong_list)


write_list = []
Correct_message = 'Correct:' + str(len(correct_list)) + str(correct_list)
Wrong_message = 'Wrong:' + str(len(wrong_list)) + str(wrong_list)
write_list.append(Correct_message)
write_list.append(Wrong_message)
text_save('Grade.txt', write_list)