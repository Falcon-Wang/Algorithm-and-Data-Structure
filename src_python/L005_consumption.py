<<<<<<< HEAD:src_python/L005_consumption.py
# 算法005：时间、空间复杂度
=======
# 算法006：时间、空间复杂度
>>>>>>> 6eadbc22c2dec32a1cc364b82eb31b3389b8ca56:src/L006_Consumption.py
import copy
import random

from src_python.L003_validator import randomArray, bubbleSort


def bubble_sort_single_loop(arr):
    """
    冒泡排序(单循环)
    此版本冒泡排序只有一个循环, 但其复杂度为O(N^2)

    @param arr: 待排序数组
    @return: 有序数组
    """
    i, end = 0, len(arr)-1  # 头指针、尾指针
    while end > 0:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        if i < end-1:   # 一轮换位结束
            i = i + 1
        else:
            end = end - 1
            i = 0
    return arr

def random_array_nonmatch(length, scale):
    """
    生成指定长度, 值在0~max之间, 且任意相邻两数不相等的随机数组
    
    @param length: 随机数组的长度
    @param scale: 随机数组的最大值
    @return: 生成的随机数组
    """
    arr = []
    arr.append((int)(random.random() * scale))
    for i in range(length-1):
        item = int(random.random() * scale)
        while True:
            if not arr[i] == item:
                arr.append(item)
                break
            else:
                item = int(random.random() * scale)
    return arr


def main():
    N, V, loop = 1000, 1000, 10
    
    print("测试开始")

    while loop > 0:
        randomLength = (int)(random.random() * N)
        arr = randomArray(randomLength, V)
        arr1 = copy.deepcopy(arr)
        arr2 = copy.deepcopy(arr)

        if not bubble_sort_single_loop(arr1) == bubbleSort(arr2):
            print("错误")

        loop = loop - 1
    print("测试结束")

    print(random_array_nonmatch(5, 10))

if __name__ == "__main__":
    main()