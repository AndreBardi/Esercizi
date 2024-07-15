def intersection(nums1: list[int], nums2: list[int]) -> list[int]:

    #nums1 = [2,2,4,2,1]
    #nums2 = [1,1,2,0,2,1,2]
    #return [1,2]
    elementi_comuni: list[int] = []
    for num in nums1:
        if num in nums2 and num not in elementi_comuni:
            elementi_comuni.append(num)
    return elementi_comuni
nums1 = [2,2,4,2,1]
nums2 = [1,1,2,0,2,1,2]
print(intersection(nums1, nums2))