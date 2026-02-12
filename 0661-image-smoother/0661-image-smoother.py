class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        num_rows = len(img)
        num_cols = len(img[0])
        
        smooth_img = [[0] * num_cols for _ in range(num_rows)]

        for row in range(num_rows):
            for col in range(num_cols):
                total_sum = 0
                pixel_count = 0
                
                for r in range(max(0, row - 1), min(num_rows, row + 2)):
                    for c in range(max(0, col - 1), min(num_cols, col + 2)):
                        total_sum += img[r][c]
                        pixel_count += 1
                
                smooth_img[row][col] = total_sum // pixel_count
                
        return smooth_img