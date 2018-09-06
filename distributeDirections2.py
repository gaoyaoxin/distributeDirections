## 开始设置
MODE = '2'
## 1 继续
# 跳过方向码有问题的考生，该考生不会进入录取程序。

## 1.1 不管
# 方向码有问题的考生用错误的方向码进入录取程序，这样可能导致其不会被录取。

## 2 跳出
# 遇到有问题的方向码，终止整个录取程序。

#  各方向名称
DIRECTION_1 = '文学'
DIRECTION_2 = '语言学'
DIRECTION_3 = '社会学'
DIRECTION_4 = '国际政治与经济'
DIRECTION_5 = '翻译'

# 各方向名额限制
# 文学
DIRECTION_1_CAPACITY = 31
# 语言学
DIRECTION_2_CAPACITY = 31
# 社会学
DIRECTION_3_CAPACITY = 31
# 国际政治与经济
DIRECTION_4_CAPACITY = 31
# 翻译
DIRECTION_5_CAPACITY = 31
## 设置完毕


# 初始化各方向计数
# 文学
DIRECTION_1_COUNT = 0
# 语言学
DIRECTION_2_COUNT = 0
# 社会学
DIRECTION_3_COUNT = 0
# 国际政治与经济
DIRECTION_4_COUNT = 0
# 翻译
DIRECTION_5_COUNT = 0


nameWithDirectionCodeTxtFileNameInput = 'nameWithDirectionCode'
nameWithDirectionCodeTxtFileNameInUse = nameWithDirectionCodeTxtFileNameInput + '.txt'


# nameWithDirectionCode
# 计算行数
fo_rU_nameWithDirectionCodeTxt = open(nameWithDirectionCodeTxtFileNameInUse, 'rU', encoding='UTF-8')

LINE_COUNT = 0
for LINE_COUNT, line in enumerate(fo_rU_nameWithDirectionCodeTxt):
	LINE_COUNT += 1

fo_rU_nameWithDirectionCodeTxt.close()

# 创建列表
fo_r_nameWithDirectionCodeTxt = open(nameWithDirectionCodeTxtFileNameInUse, 'r', encoding='UTF-8')

nameWithDirectionCodeList = []
for line, content in enumerate(fo_r_nameWithDirectionCodeTxt):
	if line in range(0, LINE_COUNT):
		nameWithDirectionCodeList.append(content.strip('\n'))

fo_r_nameWithDirectionCodeTxt.close()


for i in nameWithDirectionCodeList:
# 检查方向代码有效性
    nameAndID = i[:-5]
    directionCode = i[-5:]
    directionCodeList=[]
    for j in range(len(directionCode)):
        directionCodeList.append(directionCode[j])
    #print(directionCodeList)
    
    if directionCodeList[0] not in ['1', '2', '3', '4', '5']:
        print(nameAndID + '同学方向码 ' + directionCode + ' 第 1 位无效，因为其不是 1-5 的数字。') # index()只能找到第一个值的位置，因此 for 循环不写作 for i in directionCodeList，再找 directionCodeList.index(i)
    if directionCodeList[1] not in ['1', '2', '3', '4', '5']:
        print(nameAndID + '同学方向码 ' + directionCode + ' 第 2 位无效，因为其不是 1-5 的数字。') # index()只能找到第一个值的位置，因此 for 循环不写作 for i in directionCodeList，再找 directionCodeList.index(i)
    if directionCodeList[2] not in ['1', '2', '3', '4', '5']:
        print(nameAndID + '同学方向码 ' + directionCode + ' 第 3 位无效，因为其不是 1-5 的数字。') # index()只能找到第一个值的位置，因此 for 循环不写作 for i in directionCodeList，再找 directionCodeList.index(i)
    if directionCodeList[3] not in ['1', '2', '3', '4', '5']:
        print(nameAndID + '同学方向码 ' + directionCode + ' 第 4 位无效，因为其不是 1-5 的数字。') # index()只能找到第一个值的位置，因此 for 循环不写作 for i in directionCodeList，再找 directionCodeList.index(i)
    if directionCodeList[4] not in ['1', '2', '3', '4', '5']:
        print(nameAndID + '同学方向码 ' + directionCode + ' 第 5 位无效，因为其不是 1-5 的数字。') # index()只能找到第一个值的位置，因此 for 循环不写作 for i in directionCodeList，再找 directionCodeList.index(i)

    if len(set(directionCodeList)) != 5:
        print(nameAndID + '同学第 ' + str({'1', '2', '3', '4', '5'} - set(directionCodeList)) + ' 志愿不在方向码 ' + directionCode + ' 中，请检查。')

    errorConditions = (directionCodeList[0] not in ['1', '2', '3', '4', '5']) or (directionCodeList[1] not in ['1', '2', '3', '4', '5']) or (directionCodeList[2] not in ['1', '2', '3', '4', '5']) or (directionCodeList[3] not in ['1', '2', '3', '4', '5']) or (directionCodeList[4] not in ['1', '2', '3', '4', '5']) or (len(set(directionCodeList)) != 5)

    ## 无错
    if not errorConditions:
        print(nameAndID + '同学方向码无误，将进入录取程序。')

    ## 1.继续
    if MODE == '1' and errorConditions:
        print('跳过此考生，此考生没有进入录取程序。')
        continue
    ## 1.1不管
    if MODE == '1.1' and errorConditions:
        print('此考生将以错误的方向码进入录取程序，这样可能导致录取程序出错。')
    ## 2.跳出
    if MODE == '2' and errorConditions:
        print('因此考生方向码有误，录取程序终止。')
        break


    #print(directionCode)
    Choice_No_1 = str(directionCode.find('1') + 1)
    #print(Choice_No_1)
    Choice_No_2 = str(directionCode.find('2') + 1)
    Choice_No_3 = str(directionCode.find('3') + 1)
    Choice_No_4 = str(directionCode.find('4') + 1)
    Choice_No_5 = str(directionCode.find('5') + 1)

    # 第一志愿
    if Choice_No_1 == '1' and DIRECTION_1_COUNT < DIRECTION_1_CAPACITY:
        print(i[:-5], '第一志愿录取到', DIRECTION_1, '专业排名：', DIRECTION_1_COUNT + 1)
        DIRECTION_1_COUNT += 1
    elif Choice_No_1 == '2' and DIRECTION_2_COUNT < DIRECTION_2_CAPACITY:
        print(i[:-5], '第一志愿录取到', DIRECTION_2, '专业排名：', DIRECTION_2_COUNT + 1)
        DIRECTION_2_COUNT += 1
    elif Choice_No_1 == '3' and DIRECTION_3_COUNT < DIRECTION_3_CAPACITY:
        print(i[:-5], '第一志愿录取到', DIRECTION_3, '专业排名：', DIRECTION_3_COUNT + 1)
        DIRECTION_3_COUNT += 1
    elif Choice_No_1 == '4' and DIRECTION_4_COUNT < DIRECTION_4_CAPACITY:
        print(i[:-5], '第一志愿录取到', DIRECTION_4, '专业排名：', DIRECTION_4_COUNT + 1)
        DIRECTION_4_COUNT += 1
    elif Choice_No_1 == '5' and DIRECTION_5_COUNT < DIRECTION_5_CAPACITY:
        print(i[:-5], '第一志愿录取到', DIRECTION_5, '专业排名：', DIRECTION_5_COUNT + 1)
        DIRECTION_5_COUNT += 1

    # 第二志愿
    elif Choice_No_2 == '1' and DIRECTION_1_COUNT < DIRECTION_1_CAPACITY:
        print(i[:-5], '第二志愿录取到', DIRECTION_1, '专业排名：', DIRECTION_1_COUNT + 1)
        DIRECTION_1_COUNT += 1
    elif Choice_No_2 == '2' and DIRECTION_2_COUNT < DIRECTION_2_CAPACITY:
        print(i[:-5], '第二志愿录取到', DIRECTION_2, '专业排名：', DIRECTION_2_COUNT + 1)
        DIRECTION_2_COUNT += 1
    elif Choice_No_2 == '3' and DIRECTION_3_COUNT < DIRECTION_3_CAPACITY:
        print(i[:-5], '第二志愿录取到', DIRECTION_3, '专业排名：', DIRECTION_3_COUNT + 1)
        DIRECTION_3_COUNT += 1
    elif Choice_No_2 == '4' and DIRECTION_4_COUNT < DIRECTION_4_CAPACITY:
        print(i[:-5], '第二志愿录取到', DIRECTION_4, '专业排名：', DIRECTION_4_COUNT + 1)
        DIRECTION_4_COUNT += 1
    elif Choice_No_2 == '5' and DIRECTION_5_COUNT < DIRECTION_5_CAPACITY:
        print(i[:-5], '第二志愿录取到', DIRECTION_5, '专业排名：', DIRECTION_5_COUNT + 1)
        DIRECTION_5_COUNT += 1

    # 第三志愿
    elif Choice_No_3 == '1' and DIRECTION_1_COUNT < DIRECTION_1_CAPACITY:
        print(i[:-5], '第三志愿录取到', DIRECTION_1, '专业排名：', DIRECTION_1_COUNT + 1)
        DIRECTION_1_COUNT += 1
    elif Choice_No_3 == '2' and DIRECTION_2_COUNT < DIRECTION_2_CAPACITY:
        print(i[:-5], '第三志愿录取到', DIRECTION_2, '专业排名：', DIRECTION_2_COUNT + 1)
        DIRECTION_2_COUNT += 1
    elif Choice_No_3 == '3' and DIRECTION_3_COUNT < DIRECTION_3_CAPACITY:
        print(i[:-5], '第三志愿录取到', DIRECTION_3, '专业排名：', DIRECTION_3_COUNT + 1)
        DIRECTION_3_COUNT += 1
    elif Choice_No_3 == '4' and DIRECTION_4_COUNT < DIRECTION_4_CAPACITY:
        print(i[:-5], '第三志愿录取到', DIRECTION_4, '专业排名：', DIRECTION_4_COUNT + 1)
        DIRECTION_4_COUNT += 1
    elif Choice_No_3 == '5' and DIRECTION_5_COUNT < DIRECTION_5_CAPACITY:
        print(i[:-5], '第三志愿录取到', DIRECTION_5, '专业排名：', DIRECTION_5_COUNT + 1)
        DIRECTION_5_COUNT += 1

    # 第四志愿
    elif Choice_No_4 == '1' and DIRECTION_1_COUNT < DIRECTION_1_CAPACITY:
        print(i[:-5], '第四志愿录取到', DIRECTION_1, '专业排名：', DIRECTION_1_COUNT + 1)
        DIRECTION_1_COUNT += 1
    elif Choice_No_4 == '2' and DIRECTION_2_COUNT < DIRECTION_2_CAPACITY:
        print(i[:-5], '第四志愿录取到', DIRECTION_2, '专业排名：', DIRECTION_2_COUNT + 1)
        DIRECTION_2_COUNT += 1
    elif Choice_No_4 == '3' and DIRECTION_3_COUNT < DIRECTION_3_CAPACITY:
        print(i[:-5], '第四志愿录取到', DIRECTION_3, '专业排名：', DIRECTION_3_COUNT + 1)
        DIRECTION_3_COUNT += 1
    elif Choice_No_4 == '4' and DIRECTION_4_COUNT < DIRECTION_4_CAPACITY:
        print(i[:-5], '第四志愿录取到', DIRECTION_4, '专业排名：', DIRECTION_4_COUNT + 1)
        DIRECTION_4_COUNT += 1
    elif Choice_No_4 == '5' and DIRECTION_5_COUNT < DIRECTION_5_CAPACITY:
        print(i[:-5], '第四志愿录取到', DIRECTION_5, '专业排名：', DIRECTION_5_COUNT + 1)
        DIRECTION_5_COUNT += 1

    # 第五志愿
    elif Choice_No_5 == '1' and DIRECTION_1_COUNT < DIRECTION_1_CAPACITY:
        print(i[:-5], '第五志愿录取到', DIRECTION_1, '专业排名：', DIRECTION_1_COUNT + 1)
        DIRECTION_1_COUNT += 1
    elif Choice_No_5 == '2' and DIRECTION_2_COUNT < DIRECTION_2_CAPACITY:
        print(i[:-5], '第五志愿录取到', DIRECTION_2, '专业排名：', DIRECTION_2_COUNT + 1)
        DIRECTION_2_COUNT += 1
    elif Choice_No_5 == '3' and DIRECTION_3_COUNT < DIRECTION_3_CAPACITY:
        print(i[:-5], '第五志愿录取到', DIRECTION_3, '专业排名：', DIRECTION_3_COUNT + 1)
        DIRECTION_3_COUNT += 1
    elif Choice_No_5 == '4' and DIRECTION_4_COUNT < DIRECTION_4_CAPACITY:
        print(i[:-5], '第五志愿录取到', DIRECTION_4, '专业排名：', DIRECTION_4_COUNT + 1)
        DIRECTION_4_COUNT += 1
    elif Choice_No_5 == '5' and DIRECTION_5_COUNT < DIRECTION_5_CAPACITY:
        print(i[:-5], '第五志愿录取到', DIRECTION_5, '专业排名：', DIRECTION_5_COUNT + 1)
        DIRECTION_5_COUNT += 1

    # 未录取
    else: print(i[:-5], '未录取到合适专业')


print(DIRECTION_1, '总名额', DIRECTION_1_CAPACITY, '.录取人数：', DIRECTION_1_COUNT)
print(DIRECTION_2, '总名额', DIRECTION_2_CAPACITY, '.录取人数：', DIRECTION_2_COUNT)
print(DIRECTION_3, '总名额', DIRECTION_3_CAPACITY, '.录取人数：', DIRECTION_3_COUNT)
print(DIRECTION_4, '总名额', DIRECTION_4_CAPACITY, '.录取人数：', DIRECTION_4_COUNT)
print(DIRECTION_5, '总名额', DIRECTION_5_CAPACITY, '.录取人数：', DIRECTION_5_COUNT)
print('总考生数量：', len(nameWithDirectionCodeList))
print('总招生计划：', DIRECTION_1_CAPACITY+DIRECTION_2_CAPACITY+DIRECTION_3_CAPACITY+DIRECTION_4_CAPACITY+DIRECTION_5_CAPACITY)