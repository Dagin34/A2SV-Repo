def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    for i in range(len(heights)):
        min_index = i
        
        for j in range(i + 1, len(heights)):
            if heights[j] < heights[min_index]:
                min_index = j
        
        heights[i], heights[min_index] = heights[min_index], heights[i]
        names[i], names[min_index] = names[min_index], names[i]
    
    return names

print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))