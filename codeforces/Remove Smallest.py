total_test_cases = int(input())
 
for i in range(total_test_cases):
    array_length = int(input()) 
    numbers = list(map(int, input().split()))
    numbers.sort()
    can_reduce_to_one = True
    for i in range(len(numbers) - 1):
        current_value = numbers[i]
        next_value = numbers[i + 1]
 
        if next_value - current_value > 1:
            can_reduce_to_one = False
            break
 
    if can_reduce_to_one:
        print("YES")
    else:
        print("NO")
