def find_duplicates(list1, list2, list3):
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    common_elements = set1.intersection(set2, set3)

    common_elements_list = list(common_elements)

    return common_elements_list

list1 = [1, 2, 3, 4, 5, 5]
list2 = [4, 5, 6, 7]
list3 = [5, 7, 8]

duplicates = find_duplicates(list1, list2, list3)

if len(duplicates) > 0:
    print("Duplicates found:", duplicates)
else:
    print("No duplicates found.")
