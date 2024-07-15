def move_zeros(nums: list[int]):
    """
    Data una lista nums di interi, spostare gli zeri ala fine di questa lista
    mantenendo l'ordine originale dei numeri che non sono zeri

    Esempio 1:
    nums = [0,1,0,3,12] -> modificare la lista in [1,3,12,0,0]

    Esempio 2:
    nums = [0] -> la modifica è nulla perchè abbiamo uno zero che non si sposta
  """
    count_zero = 0
    for i in nums:
        if i != 0:
            nums[count_zero] = i
            count_zero += 1
    for i in range(count_zero, len(nums)):
        nums[i] = 0
    return nums
nums = [0]
print(move_zeros(nums))