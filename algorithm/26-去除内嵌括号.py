# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/24  4:53 下午
"""


# 一是判断已有括号是否合理，而是去除内嵌括号
def judge_is_kh_heli(strs):
    '''
    判断括号是否合理
    :param strs:
    :return:
    '''
    list_strs = list(strs)
    if list_strs[0] != '(' and list_strs[-1] != ')':
        return False
    i = 0
    kh_number = 0
    while i < len(list_strs):
        print(i)
        if list_strs[i] == '(':
            kh_number += 1
        if list_strs[i] == ')':
            kh_number -= 1
        i += 1
    if kh_number == 0:
        return True
    else:
        return False

def remove_bracket(strs):
    strs_list=list(strs)
    i=0
    str_new=[]
    while i<len(strs_list):
        if strs_list[i] not in ['(',')']:
            str_new.append(strs_list[i])
        i+=1
    return ['(']+str_new+[')']

if __name__ == '__main__':
    strs = "(1,(2,3),(4,(5,6),7))"
    flag = judge_is_kh_heli(strs)
    print('括号是否合理:',flag)
    str_new=remove_bracket(strs)
    print('str_new',''.join(str_new))