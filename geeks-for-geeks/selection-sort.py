class Solution: 
    def selectionSort(self, arr):
        size = len(arr)
        for i in range(size):
            min = arr[i]
            for j in range(i, size):
                if arr[j] < min:
                    min, arr[j] = arr[j], min
            arr[i] = min
