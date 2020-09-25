# -*-coding:utf-8-*- 
"""
@Author  : llame
@Software: PyCharm
@Time    : 2020/9/25  4:36 下午
"""
def combinationCount(n):
    number=0
    for i in range(0,n+1):
        for j in range(0,(n-i)//2+1):
            for k in range(0,(n-i-2*j)//5+1):
                if i+2*j+5*k==n:
                    number+=1
    print(number)
    return number


if __name__ == "__main__":
    print(combinationCount(100))
