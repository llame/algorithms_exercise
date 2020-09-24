# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/24  3:37 下午
"""

def findBin(arr, data) :
    if arr == None :
        return False
    i = 0
    rows = len(arr)
    cols = len(arr[0])
    j = cols - 1
    while i<rows and j>=0 :
        if arr[i][j] == data :
            return True
        elif arr[i][j] > data :
            j -= 1
        else:
            i += 1
    return False

if __name__ == '__main__' :
    arr = [[0,1,2,3,4],
           [10,11,12,13,14],
           [20,21,22,23,24],
           [30,31,32,33,34],
           [40,41,42,43,44]]
    print(findBin(arr,7))
    print(findBin(arr,33))