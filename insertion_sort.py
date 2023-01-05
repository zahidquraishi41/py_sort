def insertion_sort(arr: list) -> None:
    for i in range(1, len(arr)):
        j = i
        key = arr[j]
        while j > 0 and key < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key

if __name__ == '__main__':
    data = [10, 24, 2, 14, 400, 42, 30]
    print('Before sorting: ')
    print(data)
    insertion_sort(data)
    print('After sorting: ')
    print(data)
