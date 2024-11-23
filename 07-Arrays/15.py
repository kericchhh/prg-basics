# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n-1]

# Returns a string with day meal names separated by commas
def day_meal_plan(meal_plan, day_number):
    day_meals = meal_plan[day_number - 1]  # Get the meals for the specific day
    return ", ".join(day_meals)  # Combine meals into a single string separated by commas

# Prints weekly meal plan
print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")
for day_number in range(1, 8):  # Loop through days 1 to 7
    day_name = weekday(day_number)  # Get the day name
    meals = day_meal_plan(meal_plan, day_number)  # Get the meals for the day
    print(f"{day_name}: {meals}")  # Print the day and its meal plan
