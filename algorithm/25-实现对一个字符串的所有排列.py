# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/24  4:27 下午
"""
def swap(str,i,j):
    tmp=str[i]
    str[i]=str[j]
    str[j]=tmp
def Permutation(str,start):
    if str==None or start<0:
        return
    if start==len(str)-1:
        print(" ".join(str))
    else:
        i=start
        while i<len(str):
            swap(str,start,i)
            Permutation(str,start+1)
            swap(str,start,i)
            i+=1
def Permutation_transe(s):
    str=list(s)
    Permutation(str,0)
if __name__=='__main__':
    s='abc'
    Permutation_transe(s)