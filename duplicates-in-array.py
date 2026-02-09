def findDuplicates(nums: list[int]) -> list[int]:
    output = {}
    for num in nums:
        if num in output:
            output[num] += 1
        else:
            output[num] = 1
    
    return [out for out, count in output.items() if count > 1]

print(findDuplicates([4,3,2,7,8,2,3,1]))