def has_sublist_with_sum_zero(nums):
    sum_set = set()
    current_sum = 0
    
    for num in nums:
        current_sum += num
        
        if current_sum == 0 or current_sum in sum_set:
            return True
        
        sum_set.add(current_sum)
    
    return False

my_list = [4, 2, -3, 1, 6]
result = has_sublist_with_sum_zero(my_list)
if result:
    print("There is a sub-list with sum equal to zero.")
else:
    print("There is no sub-list with sum equal to zero.")


