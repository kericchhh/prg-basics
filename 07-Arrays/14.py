# Weekly expenses for different categories
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

category_totals = [0, 0 , 0]
week_totals = [0, 0, 0, 0]
monthly_total = 0
# Calculates expenses
for week_index, week in enumerate(monthly_expenses):
    for category_index, expence in enumerate(week):
        category_totals[category_index] += expence
        week_totals[week_index] += expence
        monthly_total += expence
        
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',category_totals[0])
print('Transport:',category_totals[1])
print('Utilities:',category_totals[2])
print('Week 1:',week_totals[0])
print('Week 2:',week_totals[1])
print('Week 3:',week_totals[2])
print('Week 4:',week_totals[3])
print('---------------')
print('TOTAL:',monthly_total)