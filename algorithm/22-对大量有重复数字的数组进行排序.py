# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/24  2:48 下午
"""

# hash法
def sort_hash(arr):
    b=dict()
    for i in range(len(arr)):
        if arr[i] in b:
            b[arr[i]]+=1
        else:
            b[arr[i]]=1
    c=list(b.keys())
    sort_quick(c,0,len(c)-1)

    sorted_list=[]
    for i in c:
        while(b[i]>0):
            sorted_list.append(i)
            b[i]-=1
    print('sorted_list',sorted_list)
    return sorted_list


def sort_quick(lists, low, high):
    if low >= high:
        return lists
    i, j = low, high
    key = lists[low]
    while (low < high):
        while (low < high and key <= lists[high]):
            high = high - 1
        lists[low] = lists[high]
        while (low < high and key >= lists[low]):
            low = low + 1
        lists[high] = lists[low]
    lists[low] = key
    sort_quick(lists, i, low - 1)
    sort_quick(lists, low + 1, j)


if __name__ == '__main__':
    arr = [16, 13, 16, 3, 3, 13, 3, 4, 13, 101, 4, 4]
    sort_quick(arr,0,len(arr)-1)
    print('arr',arr)
    sorted_arr=sort_hash(arr)
    print('sorted_arr',sorted_arr)



