def calculate_ranks(grades):
    grades.sort()  # Unique grades in descending order
    grades_to_rank = {}

    n = len(grades)
    for g in grades:
        grades_to_rank[g] = n
        n = n - 1

    ranks = [grades_to_rank[grade] for grade in grades]
    
    return ranks[::-1]


grades = list(map(int, input("Enter the grades separated by spaces: ").split()))
ranks = calculate_ranks(grades)
print("Ranks of students:", ranks)
