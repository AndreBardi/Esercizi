def mergeSort(lista: list) -> list:

    if len(lista) == 1:
        return lista

    mid: int = len(lista) // 2

    mergeSort(lista=lista[::mid])
    mergeSort(lista=lista[mid::])


if __name__ == "__main__":

    lista : list[int] = [0, 1, 2, 3, 4, 5, 6, 7]
    mergeSort(lista=lista)

def merge(list_1 : list[int], list_2: list[int]) -> list:



    i, j = 0, 0
    
    result : list[int] = [None for _ in range(len(list_1 + list_2))]

    for k in range(len(result)):

        if list_1[i] > list_2[i]:
            