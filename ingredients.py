from file_utils import write_csv_file, write_json_file, read_json_file

# ingredients menu
def ingredients_menu(ingredients_list):
    while True: 
        print("\n--- Ingredients Menu ---")
        print("1. View ingredients")
        print("2. Search ingredients")
        print("3. Search by calories")
        print("4. Add ingredient")
        print("5. Edit ingredient")
        print("6. Delete ingredient")
        print("0. Back to main menu")
        choice = input("Choice: ")
        if choice=="1": view_ingredients(ingredients_list)
        elif choice=="2": search_ingredients(ingredients_list)
        elif choice=="3": search_ingredients_by_calories(ingredients_list)
        elif choice=="4": add_ingredient(ingredients_list)
        elif choice=="5": edit_ingredients(ingredients_list)
        elif choice=="6": delete_ingredient(ingredients_list)
        elif choice=="0":
            break
        else: print("Invalid.")

def save_ingredients(ingredients_list): 
    write_csv_file("ingredients.csv", ingredients_list, ["id","name","category","calories"])

def load_last_ids():
    return read_json_file("last_ids.json")

def save_last_ids(last_ids):
    write_json_file("last_ids.json", last_ids)
    
def generate_new_id(last_ids, type_):
    last_ids[type_] += 1
    save_last_ids(last_ids)
    return str(last_ids[type_])

# ingredients
def view_ingredients(ingredients_list):
    for ing in ingredients_list:
        print(f"Name: {ing['name']}")  
        print(f"Category: {ing['category']}") 
        print(f"Calories: {ing['calories']}")  
        print("-" * 40)  

def search_ingredients(ingredients_list):
    key = input("Enter ingredient name or category (or 'back' to return): ").lower()

    if key=="back":
        return
    found = False
    for ing in ingredients_list:
        if key in ing["name"].lower() or key in ing["category"].lower():  
            print(f"Name: {ing['name']}, Category: {ing['category']}, Calories: {ing['calories']}")  
            found = True
    if not found:  
        print("No ingredients found.")

def search_ingredients_by_calories(ingredients_list):
    min_cal_input = input("Minimum calories (or 'back' to cancel): ")
    if min_cal_input.lower()=="back":
        return
    min_cal = int(min_cal_input)
    max_cal_input = input("Maximum calories (or 'back' to cancel): ")
    if max_cal_input.lower()=="back":
        return
    max_cal = int(max_cal_input) 
    found = False
    for ing in ingredients_list:
        cal = int(ing["calories"])
        if cal>=min_cal and cal<=max_cal:  
            print(f"Name: {ing['name']}, Category: {ing['category']}, Calories: {ing['calories']}")  
            found = True
    if not found:  
        print("No ingredients found.")

def add_ingredient(ingredients_list):
    last_ids = load_last_ids()
    Id = generate_new_id(last_ids, "ingredients")
    
    # Validate ingredient name - cannot be empty
    while True:
        name = input("Enter ingredient name (or 'back' to cancel): ")
        if name.lower()=="back":
            print("Cancelled.")
            return
        if name.strip():
            break
        print("Ingredient name cannot be empty! Please enter a valid name.")
    
    # Validate category - cannot be empty
    while True:
        category = input("Enter ingredient category: ")
        if category.strip():
            break
        print("Category cannot be empty! Please enter a valid category.")
    
    # Validate calories - must be a positive number
    while True:
        calories = input("Enter calories: ")
        if calories.isdigit() and int(calories) > 0:
            break
        if calories.isdigit() and int(calories) == 0:
            print("Calories must be a positive number (greater than 0)!")
        else:
            print("Calories must be a valid positive number!")
    
    ingredient = {"id": Id, "name": name, "category": category, "calories": calories}
    ingredients_list.append(ingredient)
    save_ingredients(ingredients_list)
    print(f"Ingredient '{name}' added with ID {Id}!")

def edit_ingredients(ingredients_list):
    ingredient_name = input("Enter ingredient name (or 'back' to cancel): ")
    if ingredient_name.lower()=="back":
        print("Cancelled.")
        return
    for ing in ingredients_list:
        if ing["name"]==ingredient_name:
            change = input("Enter field to change (name, category, calories): ").lower()  
            if change not in ["name","category","calories"]:  
                print("Invalid.")
                return
            if change=="calories":
                # Validate calories - must be positive number
                while True:
                    new_value = input("Enter new value: ")
                    if new_value.isdigit() and int(new_value) > 0:
                        ing[change]=new_value
                        break
                    if new_value.isdigit() and int(new_value) == 0:
                        print("Calories must be a positive number (greater than 0)!")
                    else:
                        print("Calories must be a valid positive number!")
            elif change=="name":
                # Validate name - cannot be empty
                while True:
                    new_value = input("Enter new value: ")
                    if new_value.strip():
                        ing[change] = new_value
                        break
                    print("Name cannot be empty!")
            elif change=="category":
                # Validate category - cannot be empty
                while True:
                    new_value = input("Enter new value: ")
                    if new_value.strip():
                        ing[change] = new_value
                        break
                    print("Category cannot be empty!")
            save_ingredients(ingredients_list)  
            print("Updated!")
            return
    print("Ingredient not found.") 

def delete_ingredient(ingredients_list):
    ingredient_id = input("Enter ingredient ID to delete (or 'back' to cancel): ")
    if ingredient_id.lower()=="back":
        print("Cancelled.")
        return
    for ing in ingredients_list:
        if ing["id"]==ingredient_id: 
            confirm = input(f"Really delete '{ing['name']}'? (y/n): ").lower()  
            if confirm in ["y", "yes"]:
                ingredients_list.remove(ing)  
                save_ingredients(ingredients_list) 
                print("Deleted!")
            return
    print("Not found.")

