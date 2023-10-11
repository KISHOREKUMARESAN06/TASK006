def find_minimum_element(sorted_list):
    if len(sorted_list) == 0:
        return None 

    return sorted_list[0]

sorted_list = [1, 2, 3, 4, 5]
minimum_element = find_minimum_element(sorted_list)
if minimum_element is not None:
    print(f"The minimum element is: {minimum_element}")
else:
    print("The list is empty.")
