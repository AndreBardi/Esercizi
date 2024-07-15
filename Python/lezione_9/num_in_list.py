def rotate_left(elements: list, k: int) -> list:
    elements = []

    if k == 0:
        return elements

    k = k(len(elements))
    return elements[k: ] + elements[ :k]
    

print(rotate_left([1, 2, 3, 4 ,5], 2))

