def binary_search(array: list[int], x: int) -> int:
    return __binary_search(array, x, 0, len(array))

def __binary_search(array: list[int], x: int, low: int, high: int) -> int:
    mid = (low + high)
    if x == array[mid]:
        return mid
    else:
        if x > array[mid]:
            return __binary_search(array, x, mid + 1, high)
        else:
            return __binary_search(array, x, low, mid)