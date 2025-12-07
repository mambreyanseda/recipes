from file_utils import write_csv_file, write_json_file, read_json_file

# recipes menu
def recipes_menu(recipes_list, ingredients_list, add_ingredient_func, save_ingredients_func):
    while True:  
        print("\n--- Recipes Menu ---")
        print("1. View recipes")
        print("2. Search recipes")
        print("3. Add recipe")
        print("4. Edit recipe")
        print("5. Delete recipe")
        print("6. Count recipe calories")
        print("0. Back to main menu")
        choice = input("Choice: ")
        if choice == "1":view_recipes(recipes_list,ingredients_list)
        elif choice == "2": search_recipes(recipes_list,ingredients_list)
        elif choice == "3": add_recipe(recipes_list, ingredients_list, add_ingredient_func)
        elif choice == "4": edit_recipes(recipes_list,ingredients_list, add_ingredient_func, save_ingredients_func)
        elif choice == "5": delete_recipe(recipes_list)
        elif choice == "6": calorie_counter(recipes_list,ingredients_list)
        elif choice == "0":
           break
        else: print("Invalid choice.")

# recipe helper functions
def get_valid_categories(recipes_list):
    categories = []

    for recipe in recipes_list:
        if recipe["category"].lower() not in categories:
            categories.append(recipe["category"].lower())
    return categories

def display_valid_categories(recipes_list):
    return ", ".join(get_valid_categories(recipes_list))

def save_recipes(recipes_list):  
    recipes_to_save = []

    for recipe in recipes_list:
        recipe_copy = recipe.copy()
        recipe_copy["ingredient_ids"] = ",".join(recipe_copy["ingredient_ids"])

        recipes_to_save.append(recipe_copy)
    write_csv_file("recipes.csv", recipes_to_save, ["id","name","category","ingredient_ids","steps"])

def load_last_ids():
    return read_json_file("last_ids.json")

def save_last_ids(last_ids):
    write_json_file("last_ids.json", last_ids)

def generate_new_id(last_ids, type_):
    last_ids[type_] += 1
    save_last_ids(last_ids)

    return str(last_ids[type_])

# recipes
def view_recipes(recipes_list, ingredients_list):

    for recipe in recipes_list:
        print(f"Name: {recipe['name']}")
        print(f"Category: {recipe['category']}")

        print("Ingredients:")
        ing_ids = recipe["ingredient_ids"]
        if ing_ids:
            for ing_id in ing_ids:
                found = False
                for ing in ingredients_list:
                    if ing["id"] == ing_id:  
                        print(f"- {ing['name']} ({ing['category']}, {ing['calories']} cal)")
                        found = True
                        break
                if not found:
                    print(f"- Ingredient ID {ing_id} not found")
        else:
            print("- None")
        print(f"Steps:\n{recipe['steps']}")
        print("-" * 40)
        
def search_recipes(recipes_list, ingredients_list):
    key = input("Enter recipe name, category, or ingredient (or 'back' to return): ").lower()

    if key=="back":
        return

    found = False
    for recipe in recipes_list:
        name_match = key in recipe["name"].lower()
        category_match = key in recipe["category"].lower()
        ingredient_match = False
        ing_ids = recipe["ingredient_ids"]
        for ing_id in ing_ids:
            for ing in ingredients_list:
                if ing["id"]==ing_id and key in ing["name"].lower():
                    ingredient_match = True
                    break
            if ingredient_match:
                break
        if name_match or category_match or ingredient_match:
            print(f"ID: {recipe['id']}")
            print(f"Name: {recipe['name']}")
            print(f"Category: {recipe['category']}")
            print(f"Steps:\n{recipe['steps']}")
            print("-" * 40)
            found = True
    if not found:
        print("Can't find that recipe.")

        
def add_recipe(recipes_list, ingredients_list, add_ingredient_func):

    last_ids = load_last_ids()
    Id = generate_new_id(last_ids, "recipes")
    print(f"Assigned Recipe ID: {Id}")
    name = input("Enter recipe name (or 'back' to cancel): ")
    if name.lower()=="back":
        print("Cancelled.")
        return
    valid_categories = get_valid_categories(recipes_list)
    if valid_categories:
        while True:
            category = input(f"Enter category ({display_valid_categories(recipes_list)}): ").lower()
            if category in valid_categories:
                break
            print(f"Invalid category. Choose from: {display_valid_categories(recipes_list)}.")
    else:
        category = input("Enter category: ").lower()
    steps = input("Enter recipe steps: ")

    ing_ids = []
    print("\nAvailable ingredients:")
    for ing in ingredients_list:
        print(f"{ing['id']}. {ing['name']} ({ing['category']}, {ing['calories']} cal)")

    while True:
        print("\n1. Choose ingredient by ID")
        print("2. Add new ingredient")
        print("3. Finish ingredient selection")

        choice = input("Select option: ")
        if choice=="1":
            ing_choice = input("Enter ingredient ID: ")
            for ing in ingredients_list:
                if ing["id"]==ing_choice:
                    if ing_choice not in ing_ids:
                        ing_ids.append(ing_choice)
                    print("Added!")
                    break
        elif choice=="2":
            add_ingredient_func(ingredients_list)

            new_id = ingredients_list[-1]["id"]
            if new_id not in ing_ids:
                ing_ids.append(new_id)
        elif choice=="3":
            if len(ing_ids)==0:
                print("Need at least 1 ingredient!")
            else:
                break
        else:
            print("Invalid.")

    recipe = {
        "id": Id,
        "name": name,
        "category": category,
        "ingredient_ids": ing_ids,  
        "steps": steps
    }

    recipes_list.append(recipe)
    save_recipes(recipes_list)
    print(f"Recipe '{name}' added successfully!")


def edit_recipes(recipes_list, ingredients_list, add_ingredient_func, save_ingredients_func):
    recipe_name = input("Enter recipe name (or 'back' to cancel):")
    if recipe_name.lower()=="back":
        print("Cancelled.")
        return
    for recipe in recipes_list:
        if recipe["name"].lower()==recipe_name.lower():
            while True:
                change = input("Enter field to change (name, category, steps, ingredients):").lower()
                if change=="name":
                    recipe["name"] = input("Enter new name:")

                elif change=="category":
                    valid_categories = get_valid_categories(recipes_list)
                    while True:
                        new_category = input(f"Enter new category ({display_valid_categories(recipes_list)}):").lower()
                        if new_category in valid_categories:
                            recipe["category"]=new_category
                            break
                        print(f"Invalid. Choose from: {display_valid_categories(recipes_list)}.")

                elif change=="steps":
                    recipe["steps"] = input("Enter new steps:")

                elif change=="ingredients":
                    selected_ids = []
                    while True:
                        for ing in ingredients_list:
                            print(f"{ing['id']}. {ing['name']} ({ing['category']}, {ing['calories']} cal)")
                        choice = input("Enter ingredient ID to add or 'new' to create ingredient:").lower()
                        if choice=="new":
                            add_ingredient_func(ingredients_list)
                        elif choice.isdigit():
                            for ing in ingredients_list:
                                if ing["id"]==choice:
                                    if choice not in selected_ids:
                                        selected_ids.append(choice)
                                        print(f"Added ingredient {choice}")
                                    else:
                                        print("Already selected.")
                                    break
                        else:
                            print("Invalid.")
                        finish_ing = input("Type 'done' to finish ingredient selection or Enter to continue:").lower()
                        if finish_ing=="done":
                            break
                    recipe["ingredient_ids"]=selected_ids
                else:
                    print("Invalid field.")
                finish_edit = input("Type 'done' to finish editing recipe or Enter to continue:").lower()
                if finish_edit=="done":
                    break
            save_recipes(recipes_list)
            save_ingredients_func(ingredients_list)

            print("Recipe updated!")
            return
    print("Recipe not found.")


def delete_recipe(recipes_list):
    recipe_name = input("Enter recipe name to delete (or 'back' to cancel): ")
    if recipe_name.lower()=="back":
        print("Cancelled.")
        return
    for recipe in recipes_list:
        if recipe["name"]==recipe_name:  
            confirm = input(f"Really delete '{recipe['name']}'? (y/n): ").lower()  
            if confirm in ["y", "yes"]:
                recipes_list.remove(recipe)  
                save_recipes(recipes_list)  
                print("Deleted!")  
            return
    print("Recipe not found.") 

def calorie_counter(recipes_list, ingredients_list):
    recipe_name = input("Enter recipe name (or 'back' to cancel): ").lower()

    if recipe_name=="back":
        return
    for recipe in recipes_list:
        if recipe["name"].lower()==recipe_name:
            total_calories = 0
            ing_ids = recipe["ingredient_ids"]

            print(recipe["id"]) # debuging
            if ing_ids:  
                for ing_id in ing_ids:
                    for ing in ingredients_list:
                        if ing["id"]==ing_id:
                            total_calories += int(ing["calories"])
                print(f"Total calories: {total_calories} cal")
            else:
                print(f"No ingredients.")
            return
    print("Recipe not found.")

