class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        
        candidate_one = None
        candidate_two = None
        count_one = 0
        count_two = 0
        
        for current_number in nums:
            if current_number == candidate_one:
                count_one += 1
            elif current_number == candidate_two:
                count_two += 1
            elif count_one == 0:
                candidate_one = current_number
                count_one = 1
            elif count_two == 0:
                candidate_two = current_number
                count_two = 1
            else:
                count_one -= 1
                count_two -= 1
        
        final_results = []
        threshold = len(nums) // 3
        
        actual_count_one = nums.count(candidate_one)
        actual_count_two = nums.count(candidate_two) if candidate_two != candidate_one else 0
        
        if actual_count_one > threshold:
            final_results.append(candidate_one)
        if actual_count_two > threshold:
            final_results.append(candidate_two)
            
        return final_results