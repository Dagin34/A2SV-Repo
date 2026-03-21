class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeros = arr.count(0)
        count = len(arr)

        i = count - 1
        j = count + zeros - 1

        while i >= 0:
            if j < count:
                arr[j] = arr[i]

            if arr[i] == 0:
                j -= 1
                if j < count:
                    arr[j] = 0

            i -= 1
            j -= 1