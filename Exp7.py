def calculate_calories(carbs, fats, proteins):
    total_calories = (carbs * 4) + (fats * 9) + (proteins * 4)
    return total_calories

# Input values
carbs = float(input("Enter grams of carbohydrates: "))
fats = float(input("Enter grams of fats: "))
proteins = float(input("Enter grams of proteins: "))

# Calculate total calories
total = calculate_calories(carbs, fats, proteins)

# Display result
print("Total Caloric Intake:", total, "calories")
