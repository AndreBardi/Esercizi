def find_lhs(nums: list[int]) -> int:
    count = {}
    max_length = 0
    
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if num - 1 in count:
            max_length = max(max_length, count[num] + count[num - 1])
        if num + 1 in count:
            max_length = max(max_length, count[num] + count[num + 1])
    
    return max_length