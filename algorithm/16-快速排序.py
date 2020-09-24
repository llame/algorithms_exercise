# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/23  3:23 下午
""" 

def quicksort(sort_list,start,end):
    if end<=start:
        return

    base=sort_list[start]
    index1=start
    index2=end
    while start<end:
        while start<end and sort_list[end]>=base:
            end=end-1
        sort_list[start]=sort_list[end]
        while start<end and sort_list[start]<=base:
            start=start+1
        sort_list[end]=sort_list[start]

    sort_list[start]=base
    quicksort(sort_list,index1,start-1)
    quicksort(sort_list,start+1,index2)

if __name__ == '__main__':
    list_1=[2,32,4,5,3,6,-1,4,4,8,2]
    start=0
    end=len(list_1)-1
    quicksort(list_1,start,end)
