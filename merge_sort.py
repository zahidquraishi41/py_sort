def __merge(left_arr: list, right_arr: list) -> list:
    i = j = 0
    sorted_arr = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1
    while i < len(left_arr):
        sorted_arr.append(left_arr[i])
        i += 1
    while j < len(right_arr):
        sorted_arr.append(right_arr[j])
        j += 1
    return sorted_arr


def merge_sort(arr: list, low: int, high: int) -> list:
    if low < high - 1:
        mid = (low + high) // 2
        left_arr = merge_sort(arr[0: mid], 0, mid)
        right_arr = merge_sort(arr[mid:high], 0, high-mid)
        sorted_arr = __merge(left_arr, right_arr)
        return sorted_arr
    return arr

if __name__ == '__main__':
    data = [10, 24, 2, 14, 400, 42, 30]
    print('Before sorting: ')
    print(data)
    data = merge_sort(data, 0, len(data))
    print('After sorting: ')
    print(data)

