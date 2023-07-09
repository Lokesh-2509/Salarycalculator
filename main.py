def calculate_salary(hours_worked):
    base_rate = 100
    daily_bonus = 15
    weekly_bonus = 25
    saturday_bonus = 0.25
    sunday_bonus = 0.5
    total_salary = 0
    total_hours = sum(hours_worked)
    for i, hours in enumerate(hours_worked):
        daily_salary = base_rate * hours
        if hours > 8:
            daily_salary += daily_bonus
        if i == 6:
            daily_salary *= (1 + saturday_bonus)
        elif i == 0:
            daily_salary *= (1 + sunday_bonus)
        total_salary += daily_salary
    if total_hours > 40:
        total_salary += (total_hours - 40) * weekly_bonus
    return int(total_salary)
hours_worked_1 = [0, 8, 8, 8, 10, 6, 0]
print("Case 1: ", calculate_salary(hours_worked_1))
hours_worked_2 = [4, 5, 0, 8, 0, 6, 0]
print("Case 2: ", calculate_salary(hours_worked_2))
hours_worked_3 = [5, 3, 6, 1, 1, 2, 3]
print("Case 3: ", calculate_salary(hours_worked_3))
