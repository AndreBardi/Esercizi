def majority_element(nums: list[int]) -> int:
    """
        Data una lista nums d n elementi, restituire l'elemento che
        compare più di n/2 volte.

        Esempio 1:
        nums = [3,2,3] -> restituire 3

        Esempio 2:
        nums = [2,2,1,1,1,2] -> restituire None
    """
    d: dict[int, int] = {}
    for i in nums:
        d[i] = nums.count(i)

        length = len(nums)
        for key in d:
            d[key] /= length
            if d[key] > 0.5:
                return key
            
    return None
nums  = [2,3,2,2,5,6,4,7,8,]
print(majority_element(nums))

"""
for i in nums:
    if nums.count(i) > len(nums) / 2:
        print(i)
        return i
return None
"""