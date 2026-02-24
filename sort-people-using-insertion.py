def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    for i in range(1, len(heights)):
        key_height = heights[i]
        key_name = names[i]
        
        j = i - 1
        
        while j >= 0 and heights[j] < key_height:
            heights[j + 1] = heights[j]
            names[j + 1] = names[j]
            j -= 1
        
        heights[j + 1] = key_height
        names[j + 1] = key_name
    return names

print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))