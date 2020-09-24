# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/24  9:22 上午
"""

class Test:
    def __init__(self):
        self.pos = 0
    def partion(self, arr, low, high):
        # 以 arr[low] 为基准把数组分成两部分
        key = arr[low]
        print('key1',key)
        print('low1',low)
        print('high1',high)

        while low < high:
            while low < high and arr[high] > key:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] <=key:
                low += 1
            arr[high] = arr[low]
        arr[low] = key
        self.pos = low
        print('pos1', self.pos)

    def getMid(self, arr):
        low = 0
        n = len(arr)
        high = n - 1
        mid = low + (high - low) // 2
        while True:
            print('mid',mid)
            print('pos',self.pos)
            # 以 arr[low] 为基准把数组分为两部分
            self.partion(arr, low, high)
            if self.pos == mid:
                break
            elif self.pos > mid:  # 继续在右半部分找
                high = self.pos - 1
            else:
                low = self.pos + 1  # 继续在左半部分找
        return arr[mid] if n % 2 != 0 else (arr[mid] + arr[mid + 1]) / 2

if __name__ == '__main__':
    arr = [7, 5, 3,11, 9,1,3,6,7]
    print('result:', Test().getMid(arr))

