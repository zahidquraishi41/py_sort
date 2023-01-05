def bubble_sort(arr: list) -> None:
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == '__main__':
    data = [10, 24, 2, 14, 400, 42, 30]
    print('Before sorting: ')
    print(data)
    bubble_sort(data)
    print('After sorting: ')
    print(data)
