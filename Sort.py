# 선택 정렬 : 배열 속 가장 작은 값을 선택해 맨 앞으로 가져온다
def selection_sort(arr):
    print("start selection_sort arr >", arr)
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
    
    return arr


# 거품 정렬 : 두 개의 반복문을 통해 앞에서부터 최댓값을 찾아 가장 뒤로 가져다 놓는다.
def bubble_sort(arr):
    print("start bubble_sort arr >", arr)
    for end in range(len(arr) - 1, 0 - 1, -1):
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        print(arr)
    
    return arr


# 삽입 정렬 : 앞에서부터 순서대로 정렬 범위에 삽입한다 (정렬 범위 : 원소들이 정렬되어있는 구역)
def insertion_sort(arr):
    print("start insertion_sort arr >", arr)
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            now = i
            while now > 0 and arr[now] < arr[now - 1]:
                arr[now], arr[now - 1] = arr[now - 1], arr[now]
                now -= 1
        print(arr)
    
    return arr


# 병합(합병) 정렬 : 배열을 최소 단위가 될 때까지 반으로 나눈 뒤, 차례로 병합해가며 정렬한다.
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    
    merged_arr = []
    low = high = 0
    while low < len(low_arr) and high < len(high_arr):
        if low_arr[low] < high_arr[high]:
            merged_arr.append(low_arr[low])
            low += 1
        else:
            merged_arr.append(high_arr[high])
            high += 1
    merged_arr += low_arr[low:]
    merged_arr += high_arr[high:]

    return merged_arr


# 퀵 정렬 : 적절한 pivot 값을 정하고 pivot보다 작은 원소는 왼쪽에, pivot보다 큰 원소는 오른쪽에 둔다.
# 그 후 왼쪽, 오른쪽 배열에 대해 다시 pivot을 정하고 같은 과정을 배열이 더 이상 나누어질 수 없을 때까지 반복한다.
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[len(arr) // 2]
    low_arr, same_arr, high_arr = [], [], []
    for val in arr:
        if val < pivot:
            low_arr.append(val)
        elif val > pivot:
            high_arr.append(val)
        else:
            same_arr.append(val)
    
    return quick_sort(low_arr) + same_arr + quick_sort(high_arr)



array = [6,5,3,1,8,7,2,4]
# sorted_arr = selection_sort(array)
# sorted_arr = bubble_sort(array)
# sorted_arr = insertion_sort(array)
# sorted_arr = merge_sort(array)
sorted_arr = quick_sort(array)
print("result >", sorted_arr)
