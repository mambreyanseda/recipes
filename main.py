import csv, json    
from file_utils import read_json_file, write_json_file, read_csv_file, write_csv_file, comma_string_to_list
from recipes import recipes_menu
from ingredients import ingredients_menu, add_ingredient, save_ingredients
from meals import meal_plan_menu

# user stuff
users_data = read_json_file("users.json")

def save_users(content):  
    write_json_file("users.json", content) 

# login stuff
def login_or_create():

    print("Welcome! Please log in or create an account.")
    while True:
        username = input("Enter username: ")
        if username in users_data:
            attempts = 3
            while attempts > 0:
                password = input("Enter password: ")
                if password==users_data[username]:
                    print(f"Welcome back, {username}!")

                    return username
                else:
                    attempts -= 1
                    if attempts > 0:
                        print(f"Wrong password! {attempts} attempts left.")
                    else:
                        print("Too many wrong attempts. Try again from the beginning.")

            continue 
        else:
            print("Username not found.")

            while True:
                choice = input("1. Enter a new username\n2. Create a new account with this username\nChoose 1 or 2: ")
                if choice=="1":
                    break  
                elif choice=="2":
                    confirmation_attempts = 3
                    while confirmation_attempts > 0:
                        password = input("Enter a password: ")
                        password_confirm = input("Confirm your password: ")
                        if password == password_confirm:
                            users_data[username] = password
                            save_users(users_data)

                            print(f"Account created successfully! Welcome, {username}!")
                            return username
                        else:
                            confirmation_attempts -= 1
                            if confirmation_attempts > 0:
                                print(f"Passwords do not match! {confirmation_attempts} attempts left.")
                            else:
                                print("Too many failed attempts. Restarting from the beginning.")
                                break  
                    break  
                else:
                    print("Invalid input. Please enter 1 or 2.")

# raeding data
recipes_list = read_csv_file("recipes.csv")

for recipe in recipes_list:
    ing_ids_str = recipe["ingredient_ids"]
    recipe["ingredient_ids"] = comma_string_to_list(ing_ids_str)
    
ingredients_list = read_csv_file("ingredients.csv")

mealplan = read_json_file("meal_plan.json")  


# main menu
def main_menu():
    while True:  
        print("\n--- Main Menu ---")
        print("1. Recipes")
        print("2. Ingredients")
        print("3. Meal Plan")
        print("0. Exit")
        choice = input("Choice: ")
        if choice=="1": recipes_menu(recipes_list, ingredients_list, add_ingredient, save_ingredients)
        elif choice=="2": ingredients_menu(ingredients_list)
        elif choice=="3": meal_plan_menu(mealplan, recipes_list)
        elif choice=="0":
            print("Goodbye!")  
            break
        else: print("Invalid.")

# start teh program
login_or_create()  
main_menu()  
