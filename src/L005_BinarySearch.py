# 算法005：二分搜索
import random
import time

from L004_Validator import randomArray


def binarySearch(arr, num):
    """
    二分搜索, 找指定num

    @param arr: 有序数组
    @param num: 要寻找的key
    @return: num的索引
    """
    left = 0
    right = len(arr) - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2    # 求中点
        if arr[mid] == num:
            while arr[mid] > 0 and arr[mid-1] == num:   # 当数组中存在相同元素时，返回第一个出现的元素
                mid = mid - 1
            return mid
        elif num < arr[mid]:  # key在中点左侧
            right = mid - 1
        else:   # key在中点右侧
            left = mid + 1
    return False


def bruteForce(arr, num):
    """
    暴力搜索（用于对数器进行对照）

    @param arr: 有序数组
    @param num: 要寻找的key
    @return: num的索引
    """
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return False


def find_left(arr, num):
    """
    有序数组中找>=num的最左位置

    @param arr: 有序数组
    @param num: 要寻找的key
    @return: 最先出现的>=key的元素的索引
    """
    left, right, mid, ans = 0, len(arr)-1, 0, -1    # 左指针、右指针、中值、结果索引

    while left <= right:
        # mid = (left + right) // 2   # 中点位置
        # mid = left + (right - left) // 2    # 防止索引溢出
        mid = left + ((left + right) >> 1)  # 非负数右移一位等价于除以2
        if arr[mid] < num:  # 向右找
            left = mid + 1
        else:   # 记答案，向左二分
            ans = mid
            right = mid - 1

    return ans


def brute_force_find_left(arr, num):
    """
    有序数组中找>=num的最左位置 (暴力搜索)

    @param arr: 有序数组
    @param num: 要寻找的key
    @return: 最先出现的>=key的元素的索引
    """
    for i in range(len(arr)):
        if arr[i] >= num:
            return i
    return -1


def find_right(arr, num):
    """
    有序数组中找<=num的最右位置

    @param arr: 有序数组
    @param num: 要寻找的key
    @return: 最后出现的<=key的元素的索引
    """
    left, mid, right, ans = 0, 0, len(arr)-1, -1    # 左指针、中值、右指针、结果索引
    
    while left <= right:
        mid = left + ((right - left) >> 1)    # 中值
        if arr[mid] <= num:     # 记录答案，向右二分
            ans = mid
            left = mid + 1
        else:   # 向左二分
            right = mid -1
    return ans


def brute_force_find_right(arr, num):
    """
    有序数组中找<=num的最右位置 (暴力搜索)

    @param arr: 有序数组
    @param num: 要寻找的key
    @return: 最后出现的<=key的元素的索引
    """
    ans = -1
    for i in range(len(arr)):
        if arr[i] > num:
            ans = i - 1
            return ans
    return ans


def find_peak(arr):
    """
    峰值问题 (Leetcode 0162-Find Peak Element)
        数组长度为N, 下标[0, N-1], -1和N位置为无穷小, 任意相邻的两数都不相等
        峰值: i-1 < peak < i+1
        数组中可能存在若干峰值，返回任意峰值的索引均可
    
    @param arr: 数组(可能无序)
    """    
    if arr[0] > arr[1]:     # 检查头元素
        return 0
    elif arr[-1] > arr[-2]: # 检查尾元素
        return len(arr) - 1

    left, mid, right, peak = 1, 0, len(arr) - 2, -1     # 左指针、中值、右指针、峰值索引

    while left <= right:
        mid = left + ((right - left) >> 1)  # 中点
        if arr[mid] > arr[mid -1] and arr[mid] > arr[mid + 1]:  # 中点为峰值
            peak = mid
            break
        elif arr[mid - 1] > arr[mid]:   # 向左二分
            right = mid - 1
        elif arr[mid + 1] > arr[mid]:   # 向右二分
            left = mid + 1
    return peak


def brute_force_find_peak(arr):
    """
    峰值问题 (暴力搜索)
    """
    peak = -1   # 峰值元素下标

    if arr[0] > arr[1]:
        return 0
    elif arr[-1] > arr[-2]:
        return len(arr) - 1
    
    for i in range(1, len(arr) - 1, 1):
        if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
            peak = i
            break
    
    return peak



def main():
    
    """
    N, V, loops = 10000, 1000, 1000    # 最大长度、最大值、测试次数

    print("测试开始")


    for _ in range(loops):
        arr_rand = randomArray(N, V)    # 随机数组
        num_rand = (int)(random.random() * V)    # 随机key
        arr_rand.sort()  # 默认升序
        

        # 找<=num的最右位置
        if not find_right(arr_rand, num_rand) == brute_force_find_right(arr_rand, num_rand):
            print("错误")

        # 找>=num的最左位置
        if not find_left(arr_rand, num_rand) == brute_force_find_left(arr_rand, num_rand):
            print("错误")

        # 二分搜索
        if not binarySearch(arr_rand, num_rand) == bruteForce(arr_rand, num_rand):
            print(binarySearch(arr_rand, num_rand))
            print(bruteForce(arr_rand, num_rand))
            print("错误")

    print("测试结束")
    """

    arr = [2,4,7,3,1,5,7,8,9,5,4,3,2,2,3,4,3,4,3,4,3,4,6,8,9,1]
    start_time_BF = time.time()
    for _ in range(10000):
        brute_force_find_peak(arr)
    end_time_BF = time.time()
    print(f"Running time is {((end_time_BF - start_time_BF) / 10000) * 1000:.6f} ms")

    start_time = time.time()
    for _ in range(10000):
        find_peak(arr)
    end_time = time.time()

    print(f"Running time is {((end_time - start_time) / 10000) * 1000:.6f} ms")


if __name__ == "__main__":
    main()