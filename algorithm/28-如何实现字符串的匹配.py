# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/25  1:48 下午
""" 

#题目描述：给定主字符S与模式字符串P,判断P是否是S的子串，如果是，那么找出P在S中第一次出现的下标。
def match(s, p):
    # 检查参数的合理性
    if s == None or p == None:
        print("参数不合理")
        return -1
    slen = len(s)
    plen = len(p)

    # p肯定不是S的子串
    if slen < plen:
        return -1
    i = 0
    j = 0
    while i < slen and j < plen:
        if list(s)[i] == list(p)[j]:
            # 如果相同，那么继续比较后面的字符
            i += 1
            j += 1
        else:
            # 后退回去重新比较
            i = i - j + 1
            j = 0

            if i > slen - plen:
                return -1
    # 匹配成功
    if j >= plen:
        return i - plen
    return -1


if __name__ == "__main__":
    s = "xyzabcd"
    p = "abc"
    print(match(s, p))