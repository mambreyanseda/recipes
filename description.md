# Recipe Management Project

## What This Program Does

This is a console-based recipe management system designed for families. Each family member can create their own account with password protection, but everyone shares the same recipe collection and meal plan - just like a family shares one cookbook. The program helps manage recipes, track ingredients with nutritional information, and plan weekly meals. Everything runs in the terminal and saves data to CSV and JSON files.

## How to Use the Program

### Starting Up - Login System

When you run the program, it first asks you to login or create an account.

If you already have an account, just enter your username and password. You get 3 tries to enter the right password. If you fail all 3 times, it restarts from the beginning (I added this for security).

If you don't have an account yet, the program will ask if you want to create one. When creating a new account, you need to enter your password twice to confirm it (this prevents typos). You also get 3 attempts for this.

### Main Menu

After logging in successfully, you'll see this:

```
--- Main Menu ---
1. Recipes
2. Ingredients
3. Meal Plan
0. Exit
Choice:
```

Just type a number (0-3) to choose what you want to do. If you type anything else, you'll get an "Invalid" message.

- Type 1 to work with recipes
- Type 2 to work with ingredients  
- Type 3 to plan your meals
- Type 0 to exit the program

## The Menus Explained

### 1. Recipes Menu

When you choose 1 from the main menu, you get to the recipes section:

```
--- Recipes Menu ---
1. View recipes
2. Search recipes
3. Add recipe
4. Edit recipe
5. Delete recipe
6. Count recipe calories
0. Back to main menu
Choice:
```

You have 7 options here (0-6). Choosing 0 takes you back to the main menu.

**Option 1 - View recipes:** This shows all your saved recipes with their details including ingredients and calories.

Example of what you'll see:
```
Name: Greek Salad
Category: Lunch
Ingredients:
- Lettuce (Vegetable, 5 cal)
- Feta (Dairy, 80 cal)
- Olive Oil (Fat, 120 cal)
- Salt (Spice, 0 cal)
Steps:
Chop lettuce and vegetables, add feta, drizzle olive oil, sprinkle salt, mix well.
```

**Option 2 - Search recipes:** You can search by the recipe name, category, or even by an ingredient. 

For example, if you search for "egg":
```
Name: Pancakes
Category: Breakfast
Ingredients:
- Egg (Protein, 70 cal)
- Milk (Dairy, 50 cal)
- Salt (Spice, 0 cal)
Steps:
Mix eggs and milk, add a pinch of salt, pour batter on pan, flip when golden.
----------------------------------------

Name: Chocolate Cake
Category: Dessert
Ingredients:
- Egg (Protein, 70 cal)
- Milk (Dairy, 50 cal)
- Salt (Spice, 0 cal)
Steps:
Mix ingredients, bake at 180°C for 30 minutes.
----------------------------------------
```

It shows all recipes that contain eggs.

If nothing matches your search, you'll get:
- No results found → "Can't find that recipe."

**Option 3 - Add recipe:** This is where you create new recipes. The program asks for the recipe name, category, and cooking steps. Then it shows you all available ingredients and you can pick which ones you need. If an ingredient isn't in the system yet, you can add it right there (option 2 in the ingredient selection menu).

If you try to enter invalid data, you'll get error messages:
- Empty name → "Recipe name cannot be empty! Please enter a valid name."
- Empty category → "Category cannot be empty! Please enter a valid category."
- Empty steps → "Recipe steps cannot be empty! Please enter valid steps."

Here's what it looks like:
```
Assigned Recipe ID: 12
Enter recipe name (or 'back' to cancel): Scrambled Eggs
Enter category (lunch, dinner, breakfast, snack, dessert): breakfast
Enter recipe steps: Beat eggs with milk, heat pan with butter, cook while stirring until fluffy.

Available ingredients:
1. Egg (Protein, 70 cal)
2. Milk (Dairy, 50 cal)
3. Salt (Spice, 0 cal)
4. Lettuce (Vegetable, 5 cal)
5. Feta (Dairy, 80 cal)
6. Olive Oil (Fat, 120 cal)
7. Chicken (Protein, 200 cal)
8. Pasta (Carb, 150 cal)
9. Tomato Sauce (Vegetable, 40 cal)
10. Banana (Fruit, 90 cal)
11. Yogurt (Dairy, 60 cal)
12. Honey (Sweetener, 20 cal)
13. bibar (spice, 0 cal)
14. candy (sweets, 150 cal)
15. Sugar (Sweetener, 70 cal)
16. Water (liquid, 1 cal)

1. Choose ingredient by ID
2. Add new ingredient
3. Finish ingredient selection
Select option: 1
Enter ingredient ID: 1
Added!

1. Choose ingredient by ID
2. Add new ingredient
3. Finish ingredient selection
Select option: 1
Enter ingredient ID: 2
Added!

1. Choose ingredient by ID
2. Add new ingredient
3. Finish ingredient selection
Select option: 1
Enter ingredient ID: 3
Added!

1. Choose ingredient by ID
2. Add new ingredient
3. Finish ingredient selection
Select option: 3

Recipe 'Scrambled Eggs' added successfully!
```

**Option 4 - Edit recipe:** Change any part of a recipe (name, category, steps, or ingredients). Just type the recipe name and then what you want to change.

```
Enter recipe name (or 'back' to cancel): Greek Salad
Enter field to change (name, category, steps, ingredients): steps
Enter new steps: Chop ingredients, drizzle oil, sprinkle salt, mix well.
Type 'done' to finish editing recipe or Enter to continue: done
Recipe updated!
```

If you try to enter invalid data while editing, you'll get:
- Empty name → "Name cannot be empty!"
- Empty steps → "Steps cannot be empty!"
- Recipe not found → "Recipe not found."

**Option 5 - Delete recipe:** Removes a recipe from the system. It asks for confirmation first so you don't accidentally delete something important.

```
Enter recipe name to delete (or 'back' to cancel): Tea
Really delete 'Tea'? (y/n): yes
Deleted!
```

Possible outcomes:
- Recipe found and confirmed → "Deleted!"
- Recipe not found → "Recipe not found."
- User says anything other than 'y'/'yes' → Deletion cancelled

**Option 6 - Count recipe calories:** It adds up all the calories from the ingredients in a recipe automatically.

```
Enter recipe name (or 'back' to cancel): Greek Salad
The recipe ID is 1
Total calories: 210 cal
```

Possible outcomes:
- Recipe found → Shows ID and total calories
- Recipe not found → "Recipe not found."
- Recipe has no ingredients → "No ingredients."

### 2. Ingredients Menu

Choose 2 from the main menu to manage ingredients:

```
--- Ingredients Menu ---
1. View ingredients
2. Search ingredients
3. Search by calories
4. Add ingredient
5. Edit ingredient
6. Delete ingredient
0. Back to main menu
Choice:
```

Again, 7 options (0-6). Type 0 to go back.

**Option 1 - View ingredients:** Shows everything in your ingredient list with their categories and calories.

```
Name: Egg
Category: Protein
Calories: 70
----------------------------------------
Name: Milk
Category: Dairy
Calories: 50
----------------------------------------
Name: Salt
Category: Spice
Calories: 0
```

**Option 2 - Search ingredients:** Search by name or category. If nothing matches, it says "No ingredients found."

```
Enter ingredient name or category (or 'back' to return): dairy
Name: Milk, Category: Dairy, Calories: 50
Name: Feta, Category: Dairy, Calories: 80
Name: Yogurt, Category: Dairy, Calories: 60
```

**Option 3 - Search by calories:** This is useful if you want to find low-calorie or high-calorie ingredients. You enter a min and max calorie range.

```
Minimum calories (or 'back' to cancel): 50
Maximum calories (or 'back' to cancel): 100
Name: Milk, Category: Dairy, Calories: 50
Name: Egg, Category: Protein, Calories: 70
Name: Feta, Category: Dairy, Calories: 80
Name: Banana, Category: Fruit, Calories: 90
Name: Yogurt, Category: Dairy, Calories: 60
Name: Sugar, Category: Sweetener, Calories: 70
```

If no ingredients are found in that range, you'll get:
- No matches → "No ingredients found."

**Option 4 - Add ingredient:** Create a new ingredient. The program has validation - it won't let you enter empty names, empty categories, or zero/negative calories. 

```
Enter ingredient name (or 'back' to cancel): Butter
Enter ingredient category: Fat
Enter calories: 100
Ingredient 'Butter' added with ID 17!
```

If you try to enter invalid data, it'll keep asking until you get it right:
- Empty name → "Ingredient name cannot be empty!"
- Empty category → "Category cannot be empty!"
- Zero or negative calories → "Calories must be a positive number (greater than 0)!"

**Option 5 - Edit ingredient:** Change an ingredient's name, category, or calories.

```
Enter ingredient name (or 'back' to cancel): Salt
Enter field to change (name, category, calories): calories
Enter new value: 5
Updated!
```

Possible outcomes:
- Valid changes → "Updated!"
- Ingredient not found → "Ingredient not found."
- Invalid new values → Same validation as adding (empty fields rejected, calories must be positive)

**Option 6 - Delete ingredient:** Remove an ingredient by entering its name. It asks for confirmation.

```
Enter ingredient name to delete (or 'back' to cancel): candy
Really delete 'candy'? (y/n): y
Deleted!
```

Possible outcomes:
- Ingredient found and confirmed → "Deleted!"
- Ingredient not found → "Ingredient not found."
- User says anything other than 'y'/'yes' → Deletion cancelled

### 3. Meal Plan Menu

Choose 3 from the main menu to plan your weekly meals:

```
--- Meal Plan Menu ---
1. View meal plan
2. Add meal plan
3. Delete meal plan
0. Back to main menu
Choice:
```

This one has 4 options (0-3).

**Option 1 - View meal plan:** Enter a day of the week to see what meals you planned for that day.

```
Enter day (or 'back' to return): Sunday
Sunday:
- Chicken Pasta
```

If there's no meal planned for that day, it just says "No meal planned for this day."

**Option 2 - Add meal plan:** Choose a day and add a recipe to it.
```
Enter day (or 'back' to cancel): Sunday
Available recipes:
- Greek Salad
- Chicken Pasta
- Pancakes
- Vegetable Soup
- Avocado Toast
- Grilled Chicken
- Fruit Smoothie
- Chocolate Cake
- Caesar Salad
- Fruit Salad
- Spagetti
Enter recipe name: Chicken Pasta
Added Chicken Pasta to Sunday.
```

If you try to add a recipe that doesn't exist, you'll get:
- Non-existent recipe → "Recipe doesn't exist."

**Option 3 - Delete meal plan:** You can delete either by day (removes all meals for that day) or by recipe name (removes just that recipe). Both ask for confirmation.

Delete by recipe name:
```
Delete by day or recipe name? (day/name or 'back' to cancel): name
Enter recipe name to delete: Chicken Pasta
Delete 'Chicken Pasta' on Sunday? (y/n): y
Deleted.
```

Delete by day:
```
Delete by day or recipe name? (day/name or 'back' to cancel): day
Enter day: Sunday
Really delete all meals for Sunday? (y/n): y
Deleted meal for Sunday
```

Possible outcomes:
- Delete by name, found and confirmed → "Deleted."
- Delete by name, not found → "Not found."
- Delete by day, found and confirmed → "Deleted meal for [day]"
- Delete by day, not found → "No meal for that day."
- User says anything other than 'y'/'yes' → Deletion cancelled

## Important Things to Know

### The 'back' Option

Almost everywhere in the program, you can type 'back' to cancel what you're doing and go back to the previous menu. I added this feature because I wanted to make it user-friendly. So if you start adding a recipe but change your mind, just type 'back' and nothing gets saved.

### Input Validation

The program checks your inputs to prevent bad data:
- You can't save empty names or categories (it'll keep asking)
- Calorie values have to be positive numbers (no zero, no negatives, no letters)
- When deleting stuff, only typing 'y' or 'yes' actually deletes it. Anything else (including 'n', 'no', or random text) cancels the deletion

### How Data is Saved

Everything saves automatically to files:
- recipes.csv - all the recipes
- ingredients.csv - all the ingredients
- users.json - user accounts and passwords
- meal_plan.json - your meal plans
- last_ids.json - keeps track of ID numbers

The program saves immediately whenever you make a change, so you don't have to worry about losing your work if something crashes or you exit without "saving."

## Notes

The program is designed to be user-friendly and prevent errors. All searches and categories are case-insensitive to avoid duplicates like "Breakfast" and "breakfast", and the validation system won't let you save empty names or categories (including whitespace-only inputs like spaces or tabs) or use non-positive calories. If you try to enter an empty value, the program will show an error message and keep asking until you provide valid input. When you delete something (recipe, ingredient, or meal), it always asks for confirmation so you don't accidentally remove important data, and if you delete an ingredient that's used in recipes, those recipes will still exist but show "Ingredient not found" for that ingredient.

## About the Code

### How We Organized the Files

We splited the program into different Python files to keep things organized. 

**main.py** - This is where the program starts. It handles the login system and shows the main menu. When you run the program, this is what executes first.

**recipes.py** - All the recipe-related functions are here. View, search, add, edit, delete recipes, and the calorie counter. 

**ingredients.py** - Same idea but for ingredients. All the ingredient operations (view, search, add, edit, delete) are in this file.

**meals.py** - Handles the meal planning stuff. Adding meals to days, viewing meal plans, and deleting meals.

**file_utils.py** -  We created it to avoid repeating the same file reading/writing code everywhere. It has helper functions that the other files use.

### About file_utils.py

I made this file because I kept writing the same CSV and JSON reading/writing code over and over in different files. 

Here's what's in it:

**For JSON files (users, meal plans, ID tracking):**
- `read_json_file()` - Reads a JSON file and returns the data. If the file is empty, it returns an empty dictionary instead of crashing.
- `write_json_file()` - Writes data to a JSON file. 

**For CSV files (recipes and ingredients):**
- `read_csv_file()` - Reads a CSV file and returns a list of dictionaries. Each row becomes a dictionary.
- `write_csv_file()` - Writes a list of dictionaries to a CSV file with headers.

**Helper function:**
- `comma_string_to_list()` - This converts comma-separated ingredient IDs (like "1,2,3") into a list (["1", "2", "3"]). I needed this because CSV files store the ingredient IDs as a single string, but I need them as a list in the program. It also filters out any non-digit values and handles empty strings.

### How the Data Flows

When the program starts:
1. main.py loads all the data from the CSV and JSON files using file_utils
2. It converts the ingredient IDs in recipes from strings to lists
3. Shows the login screen
4. After login, passes the loaded data to the menu functions

When you make changes (add/edit/delete):
1. The change is made to the list in memory
2. The appropriate save function is called immediately
3. The save function uses file_utils to write back to the file

This means changes save instantly, which is nice because you don't lose work.

### ID System

Each recipe and ingredient gets a unique ID number. The last_ids.json file keeps track of the highest ID used for each type. When you add something new:
1. Program reads last_ids.json
2. Increments the appropriate counter (recipes or ingredients)
3. Assigns that number as the new ID
4. Saves the updated counter back to last_ids.json

