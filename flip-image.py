class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        n = len(image)
        for row in image:
            for i in range((n + 1) // 2):
                row[i], row[n-1-i] = 1 - row[n-1-i], 1 - row[i]
                
        return image