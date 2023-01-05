def selection_sort(arr: list) -> None:
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    data = [10, 24, 2, 14, 400, 42, 30]
    print('Before sorting: ')
    print(data)
    selection_sort(data)
    print('After sorting: ')
    print(data)
