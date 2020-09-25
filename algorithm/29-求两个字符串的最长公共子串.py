# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/25  2:00 下午
"""
#题目描述：找出两个字符串的最长公共子串。例如：‘abccade’与字符串'dgcadde'的最长公共子串为'cad'.
#动态规划

def getMaxSubStr(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    sb = ''
    maxs = 0  # 用来记录最长公共子串的长度
    maxI = 0  # 用来记录最长公共子串最后一个字符的位置
    # 申请新的空间来记录公共子串长度的信息
    M = [([None] * (len1 + 1)) for i in range(len2 + 1)]

    i = 0
    while i < len1 + 1:
        M[i][0] = 0
        i += 1

    j = 0
    while j < len2 + 1:
        M[0][j] = 0
        j += 1

    # 通过利用递归公式填写新建的二维数组（公共字串的长度信息）
    i = 1
    while i < len1 + 1:
        j = 1
        while j < len2 + 1:
            if list(str1)[i - 1] == list(str2)[j - 1]:
                M[i][j] = M[i - 1][j - 1] + 1
                if M[i][j] > maxs:
                    maxs = M[i][j]
                    maxI = i
            else:
                M[i][j] = 0
            j += 1
        i += 1

    # 找出公共字串
    i = maxI - maxs
    while i < maxI:
        sb = sb + list(str1)[i]
        i += 1

    return sb


if __name__ == "__main__":
    str1 = "abccade"
    str2 = "dgcadde"
    print(getMaxSubStr(str1, str2))