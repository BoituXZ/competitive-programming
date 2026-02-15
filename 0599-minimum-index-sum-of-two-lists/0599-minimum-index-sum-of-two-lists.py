class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        min_index_sum = float('inf')
        common_restaurants = []

        for index1 in range(len(list1)):
            restaurant1 = list1[index1]
            
            for index2 in range(len(list2)):
                restaurant2 = list2[index2]
                
                if restaurant1 == restaurant2:
                    current_sum = index1 + index2
                    
                    if current_sum < min_index_sum:
                        min_index_sum = current_sum
                        common_restaurants = [restaurant1]
                    elif current_sum == min_index_sum:
                        common_restaurants.append(restaurant1)
                        
        return common_restaurants