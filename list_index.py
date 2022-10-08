import re


# 获得能点击交互列表的标号  用来获得xpath地址  详细xpath地址规律见 xpath编号.txt 文件
def getlist(text):
    number_list0 = re.findall('class="pl5  hour">(.*?)</b>', text)
    # print(number_list0)
    # 存放拥有三级列表的二级列表
    number_list1 = []
    for i in number_list0:
        if i.count('.') == 2:
            list0 = i.split('.')
            del list0[len(list0) - 1]
            str0 = '.'.join(list0)
            if str0 not in number_list1:
                number_list1.append(str0)
    for j in number_list1:
        index0 = number_list0.index(j)
        del number_list0[index0]
    return number_list0
