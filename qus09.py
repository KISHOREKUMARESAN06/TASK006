def find_triplet_with_sum(lst, target_sum):
    n = len(lst)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == target_sum:
                    return [lst[i], lst[j], lst[k]]
    return None

lst = [10, 20, 30, 9]
target_sum = 59

result = find_triplet_with_sum(lst, target_sum)

if result:
    print("Triplet with sum {} found: {}".format(target_sum, result))
else:
    print("No triplet found with sum {}.".format(target_sum))
