# 算法004：选择、冒泡、插入排序

def selectionSort(arr):
    """
    选择排序

    @param arr: 待排序数组
    @return: 排序后的数组
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubbleSort(arr):
    """
    冒泡排序

    @param arr: 待排序数组
    @return: 排序后的数组
    """
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def bubbleSort_Reversed(arr):
    """
    冒泡排序变种（向前冒泡）

    @param arr: 待排序数组
    @return: 排序后的数组
    """
    for i in range(1, len(arr)):
        j = i - 1
        while j >=0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
    return arr


def insertionSort(arr):
    """
    插入排序
    
    @param arr: 待排序数组
    @return: 排序后的数组
    """
    for i in range(1, len(arr)):
        key = arr[i]    # 当前元素
        j = i - 1
        while j >= 0 and key < arr[j]:  # 向左遍历
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr



def main():
    arr = [2, 5, 8, 0, 1, 3, 4, 6, 7, 9]
    print("原数组：", arr)

    selectionSortResult = selectionSort(arr.copy())
    print("选择排序结果：", selectionSortResult)
    
    bubbleSortResult = bubbleSort(arr.copy())
    print("冒泡排序结果：", bubbleSortResult)
    
    bubbleSortResult_Reversed = bubbleSort_Reversed(arr.copy())
    print("反向冒泡排序结果：", bubbleSortResult_Reversed)

    insertionSortResult = insertionSort(arr.copy())
    print("插入排序结果：", insertionSortResult)

if __name__ == "__main__":
    main()