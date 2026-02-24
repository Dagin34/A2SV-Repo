def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            if heights[j] > heights[i]:
                heights[i], heights[j] = heights[j], heights[i]
                names[i], names[j] = names[j], names[i]
    return names

print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))