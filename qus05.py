def distribute_mangoes(mangoes, students):
    mangoes.sort()
    
    min_diff = float('inf')
    
    for i in range(len(mangoes) - students + 1):
        diff = mangoes[i + students - 1] - mangoes[i]
        
        min_diff = min(min_diff, diff)
    
    return min_diff

mangoes = [7, 3, 2, 4, 9, 12, 56]
students = 3
result = distribute_mangoes(mangoes, students)
print("Minimum difference between bags:", result)
