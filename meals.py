from file_utils import write_json_file

# meal plan menu
def meal_plan_menu(mealplan, recipes_list):
    while True:  
        print("\n--- Meal Plan Menu ---")
        print("1. View meal plan")
        print("2. Add meal plan")
        print("3. Delete meal plan")
        print("0. Back to main menu")
        choice = input("Choice: ")
        if choice=="1": view_meal_plan(mealplan)
        elif choice=="2": add_mealplan(mealplan, recipes_list)
        elif choice=="3": delete_meal(mealplan)
        elif choice=="0":
            break
        else: print("Invalid.")

def change_meal_plan(mealplan):  
    write_json_file("meal_plan.json", mealplan)  

# meal plans
def view_meal_plan(mealplan):
    day = input("Enter day (or 'back' to return): ")
    if day.lower()=="back":
        return
    day = day.capitalize()
    if day in mealplan:  
        print(f"{day}:")
        for r in mealplan[day]: 
            print(f"- {r}") 
    else:
        print("No meal planned for this day.")  

def add_mealplan(mealplan, recipes_list):
    day = input("Enter day (or 'back' to cancel): ")
    if day.lower()=="back":
        print("Cancelled.")
        return
    day = day.capitalize()
    print("Available recipes:")
    for r in recipes_list:  
        print(f"- {r['name']}")
    recipe_name = input("Enter recipe name: ")  
    found=False
    for r in recipes_list:
        if r["name"].lower()==recipe_name.lower():
            found=True
            break
    if not found:
        print("Recipe doesn't exist.")
        return
    if day not in mealplan:  
        mealplan[day] = []
    if recipe_name not in mealplan[day]:  
        mealplan[day].append(recipe_name)
    change_meal_plan(mealplan)  
    print(f"Added {recipe_name} to {day}.")  

def delete_meal(mealplan):
    choice = input("Delete by day or recipe name? (day/name or 'back' to cancel): ").lower()
    if choice=="back":
        print("Cancelled.")
        return
    if choice=="day":
        day = input("Enter day: ").capitalize()
        if day in mealplan:
            confirm = input(f"Really delete all meals for {day}? (y/n): ").lower()
            if confirm in ["y", "yes"]:
                mealplan.pop(day)
                change_meal_plan(mealplan)
                print(f"Deleted meal for {day}")
        else:
            print("No meal for that day.")
    elif choice=="name":
        recipe_name = input("Enter recipe name to delete: ").lower()
        found = False
        for day, meals in list(mealplan.items()): # loop thru days
            for meal in meals:
                if meal.lower()==recipe_name:
                    confirm = input(f"Delete '{meal}' on {day}? (y/n): ").lower()
                    if confirm in ["y", "yes"]:
                        meals.remove(meal)  
                        found = True
                        if not meals: 
                            del mealplan[day]
        if found:
            change_meal_plan(mealplan)
            print(f"Deleted.")
        else:
            print("Not found.")

