def __partition(arr, lb, ub):
    pivot = arr[lb]
    beg, end = lb, ub
    i = beg
    beg += 1
    while beg < end:
        if arr[beg] < pivot:
            i += 1
            arr[i], arr[beg] = arr[beg], arr[i]
        beg += 1
    arr[i], arr[lb] = arr[lb], arr[i]
    return i


def quick_sort(arr: list, lb: int, ub: int) -> None:
    if lb < ub:
        j = __partition(arr, lb, ub)
        quick_sort(arr, lb, j)
        quick_sort(arr, j + 1, ub)


if __name__ == '__main__':
    data = [10, 24, 2, 14, 400, 42, 30]
    print('Before sorting: ')
    print(data)
    quick_sort(data, 0, len(data))
    print('After sorting: ')
    print(data)
