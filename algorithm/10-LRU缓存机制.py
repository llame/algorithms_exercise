# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/22  1:49 下午
"""


# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，
# 从而为新的数据值留出空间。

class LRUCache(object):
    def __init__(self, capacity):
        '''
        :param capacity:int
        '''
        self.maxlength = capacity
        self.dic = {}
        self.array_list = []

    def get(self,key):
        value=self.dic.get(key)#
        if value is not None and self.array_list[0] is not key:# 如果密钥存在且不是不在队列首，则将其移动到队列首部
            index=self.array_list.index(value)
            self.array_list.pop(index)
            self.array_list.insert(0,key)

        value=value if value is not None else -1
        return value



    def put(self,key,value):
        """
        :param key:
        :param value:
        :return:
        """
        #如果重复
        if self.dic.get(key) is not None:
            self.dic.pop(key)
            index=self.array_list.index(key)
            self.array_list.pop(index)

        #如果队列已满
        if len(self.array_list)>=self.maxlength:
            key_delete=self.array_list.pop(self.maxlength-1)
            self.dic.pop(key_delete)

        #将元素加入dic，并更新队列
        self.dic[key]=value
        self.array_list.insert(0,key)


if __name__ == '__main__':
    cache = LRUCache(2 )
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)