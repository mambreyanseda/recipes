# Recipe Management System

## What It Does 


This is a console-based recipe managers description. You can view/search/edit/add recipes and ingredients, track calories of ingredients and recipes, and plan meals for the week. It has a login system so data is password-protected. One of the most important features is that you can type `'back'` at almost any prompt to cancel what you're doing. So you're never stuck.

## Main Features

### 1. Login System
- Create an account with username and password, if you do not have one. 
- Password confirmation to avoid typos
- 3 attempts to login before it kicks you back to start

### 2. Recipe Management
View Recipes - Shows all your recipes with ingredients and their calorie info

Search Recipes - Search by recipe name, category, or ingredient name. It's case-insensitive so "chicken" finds "Chicken" or "CHICKEN".

Add Recipe - Create new recipes by entering:
- Recipe name (required)
- Category like breakfast, lunch, dinner (required)
- Cooking steps (required)
- Select ingredients from your list or add new ones

Edit Recipe - Change the name, category, steps, or ingredients of existing recipes

Delete Recipe - Remove recipes you don't need (asks for confirmation first)

Count Calories - Automatically adds up calories from all ingredients in a recipe

### 3. Ingredient Management
View Ingredients - Lists all ingredients with their category and calories

Search Ingredients - Find by name or category

Search by Calorie Range - Enter min and max calories to find ingredients in that range

Add Ingredient - Create new ingredients with:
- Name (required)
- Category (required)
- Calories (must be a positive number)

Edit Ingredient - Update name, category, or calorie count

Delete Ingredient - Remove ingredients (asks for confirmation)

### 4. Meal Planning
View Meal Plan - Enter a day like "Monday" to see what recipes you planned

Add to Meal Plan - Assign recipes to specific days of the week

Delete from Meal Plan - Remove meals by day or by recipe name

## How to Use It

### First Time Setup

1. Run the program
2. Enter a new username
3. System says "Username not found"
4. Choose option 2 to create a new account
5. Enter and confirm your password
6. You're in!

### Main Menu

After logging in you'll see:
```
--- Main Menu ---
1. Recipes
2. Ingredients
3. Meal Plan
0. Exit
```

Just type the number and press Enter. Each submenu works the same way.

### The Back Option

Almost everywhere you can type `'back'` to cancel:
- When adding or editing recipes
- When adding or editing ingredients  
- When searching for anything
- When adding to meal plan

This makes it easy to change your mind without messing things up.

## Sample Operations

Here's what actually happens when you use the system.

### Example 1: Creating an Account and First Ingredient

```
$ python3 main.py

Welcome! Please log in or create an account.
Enter username: alex
Username not found.
1. Enter a new username
2. Create a new account with this username
Choose 1 or 2: 2
Enter a password: mypass
Confirm your password: mypass
Account created successfully! Welcome, alex!

--- Main Menu ---
1. Recipes
2. Ingredients
3. Meal Plan
0. Exit
Choice: 2

--- Ingredients Menu ---
1. View ingredients
2. Search ingredients
3. Search by calories
4. Add ingredient
5. Edit ingredient
6. Delete ingredient
0. Back to main menu
Choice: 4

Enter ingredient name (or 'back' to cancel): Chicken
Enter ingredient category: protein
Enter calories: 165
Ingredient 'Chicken' added with ID 1!
```

Result: You created an account and added your first ingredient.

---

### Example 2: Adding a Recipe

```
--- Recipes Menu ---
Choice: 3

Assigned Recipe ID: 1
Enter recipe name (or 'back' to cancel): Chicken Salad
Enter category: lunch
Enter recipe steps: Grill chicken, chop veggies, mix with dressing

Available ingredients:
1. Chicken (protein, 165 cal)
2. Lettuce (vegetable, 5 cal)
3. Tomato (vegetable, 22 cal)

1. Choose ingredient by ID
2. Add new ingredient
3. Finish ingredient selection
Select option: 1
Enter ingredient ID: 1
Added!

Select option: 1
Enter ingredient ID: 2
Added!

Select option: 3

Recipe 'Chicken Salad' added successfully!
```

Result: Created a recipe with 2 ingredients.

---

### Example 3: Searching and Counting Calories

```
--- Recipes Menu ---
Choice: 2

Enter recipe name, category, or ingredient (or 'back' to return): chicken

Name: Chicken Salad
Category: lunch
Ingredients:
- Chicken (protein, 165 cal)
- Lettuce (vegetable, 5 cal)
Steps:
Grill chicken, chop veggies, mix with dressing
----------------------------------------

--- Recipes Menu ---
Choice: 6

Enter recipe name (or 'back' to cancel): chicken salad
Total calories: 170 cal
```

Result: Found the recipe and calculated its total calories (165 + 5 = 170).

---

### Example 4: Input Validation

```
Enter ingredient name (or 'back' to cancel): 
Ingredient name cannot be empty! Please enter a valid name.
Enter ingredient name (or 'back' to cancel): Sugar
Enter ingredient category: sweetener
Enter calories: 0
Calories must be a positive number (greater than 0)!
Enter calories: -10
Calories must be a valid positive number!
Enter calories: 400
Ingredient 'Sugar' added with ID 3!
```

Result: System won't let you save empty names or invalid calorie values. It keeps asking until you enter valid data.

---

### Example 5: Using the Back Option

```
--- Recipes Menu ---
Choice: 3

Assigned Recipe ID: 5
Enter recipe name (or 'back' to cancel): back
Cancelled.

--- Recipes Menu ---
```

Result: Typed 'back' so nothing was saved. Back at the menu.

---

### Example 6: Meal Planning

```
--- Meal Plan Menu ---
Choice: 2

Enter day (or 'back' to cancel): Monday
Available recipes:
- Chicken Salad
- Pancakes
Enter recipe name: Chicken Salad
Added Chicken Salad to Monday.

--- Meal Plan Menu ---
Choice: 1

Enter day (or 'back' to return): Monday
Monday:
- Chicken Salad
```

Result: Planned Chicken Salad for Monday and viewed the plan.

## Input Validation

The system validates your input to prevent bad data:

Required Fields:
- Recipe names, categories, and steps can't be empty
- Ingredient names and categories can't be empty
- Whitespace-only input (like "   ") counts as empty

Calorie Validation:
- Must be a positive number greater than 0
- Won't accept: 0, negative numbers, or letters
- Only accepts whole numbers (no decimals)

Category Management:
- Categories are automatically lowercase
- Prevents duplicates like "Dinner" and "dinner"

## How It Works (Technical Stuff)

### File Structure
```
recipes/
├── main.py              # Login and main menu
├── recipes.py           # Recipe functions
├── ingredients.py       # Ingredient functions
├── meals.py            # Meal planning functions
├── file_utils.py       # File reading/writing helpers
├── recipes.csv         # Recipe data
├── ingredients.csv     # Ingredient data
├── users.json          # User accounts
├── meal_plan.json      # Meal plans
└── last_ids.json       # ID tracking

### Data Storage

CSV Files - Used for recipes and ingredients
- Easy to read and edit manually if needed
- Columns are clearly labeled

JSON Files - Used for users and meal plans
- Simple key-value format
- Easy to work with in Python

### How Recipes and Ingredients Connect

Recipes store ingredient IDs as comma-separated values. For example:
- Recipe has `ingredient_ids: "1,2,3"`
- When you view it, the system looks up ingredients 1, 2, and 3
- Shows their names, categories, and calories

This lets multiple recipes share the same ingredients.

### ID System
Every recipe and ingredient gets a unique ID:
- IDs start at 1 and go up
- `last_ids.json` tracks the highest ID used
- New items get the next number automatically
- No two items ever have the same ID



