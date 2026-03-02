class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            if i == x - 1:
                continue
            if i != 0:
                res.append(i + 1)
                arr[:i+1] = arr[:i+1][::-1]
            res.append(x)
            arr[:x] = arr[:x][::-1]
        return res