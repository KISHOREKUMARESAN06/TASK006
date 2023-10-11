def first_non_repeating_element(nums):
    freq_dict = {}
    
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    for num in nums:
        if freq_dict[num] == 1:
            return num
    
    return None
    
my_list = [4, 3, 2, 4, 2, 1, 3]
result = first_non_repeating_element(my_list)
if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("No non-repeating element found in the list.")
