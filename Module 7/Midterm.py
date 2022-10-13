"""def print_meals(meal_plan):
    for items in meal_plan:
        print(f"{items}: " + str(meal_plan.get(items)))
"""

def print_meals(meal_plan):
    for key in meal_plan:
        if type(key) is dict:
            print_meals(key)
        else:
            print(f"{key}: " + str(meal_plan.get(key)))



# create an empty dictionary
meal_plan = {}

# create individual dictionaries for each meal
lunch = {"sandwich": 2, "chips": 1, "drink": 1}
dinner = {"ribs": 6, "mac_cheese": 1, "roll": 1, "pie": 1}

# create a nested dictionary
meal_plan["lunch"] = lunch
meal_plan["dinner"] = dinner

# call recursive function 'print_meals'

print_meals(meal_plan)

