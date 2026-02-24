def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    max_num = max(heights)
    min_num = abs(max(heights))
    count = [0] * (min_num + max_num + 1)
    for num in heights:
        count[num + min_num] += 1
    
    target = 0
    for index, value in enumerate(count):
        for i in range(value):
            heights[target] = index - min_num
            target += 1
    
    return heights

print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))