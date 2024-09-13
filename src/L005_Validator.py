# 算法005：对数器
import random
import copy

from L004_Sort import selectionSort, bubbleSort, bubbleSort_Reversed, insertionSort

def randomArray(length, scale):
    """
    随机数组生成器
    
    @param length: 生成数组的长度
    @param scale: 数组元素的最大值
    @return: 生成的数组
    """
    arr = []
    i = 0
    while i < length:
        # random.random() 生成一个[0,1)之间的浮点数
        arr.append((int)(random.random() * scale)+1)
        i += 1
    return arr

def main():
    N = 100     # 随机数组最大长度
    V = 1000    # 随机数组元素的最大值
    loopTimes = 50000   # 测试次数

    for _ in range(loopTimes):
        randomLength = (int)(random.random() * N)   # 数组样本长度随机
        arr = randomArray(randomLength, V)  # 生成随机数组
        arr1 = copy.deepcopy(arr)   # 深拷贝，创建独立的副本
        arr2 = copy.deepcopy(arr)
        arr3 = copy.deepcopy(arr)
        arr4 = copy.deepcopy(arr)

        print("测试开始")

        selectionSort(arr1)
        bubbleSort(arr2)
        bubbleSort_Reversed(arr3)
        insertionSort(arr4)

        # 排序结果是否相同
        if not (arr1 == arr2 
                or arr1 == arr3 
                or arr1 == arr4 
                or arr2 == arr3
                or arr2 == arr4 
                or arr3 == arr4):
            print("出错了")
            # 打印出错的数组进行debug
    print("测试结束")

if __name__ == "__main__":
    main()