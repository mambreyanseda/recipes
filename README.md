# My Recipe Management System Project

So I made this recipe manager program for my intro to CS class. It lets you save recipes. You can keep track of ingredients. You can also plan out your meals for the week. It's pretty useful actually.

## What it does

First you gotta login or make an account. Then you get to the main menu. You can do stuff with recipes, ingredients, or your meal plan.

**Login part:**
- You can make a new account if you don't have one
- It makes you confirm your password. That way you don't mess it up.
- You get 3 tries to enter the right password. If you fail it kicks you back to the start. I learned that from my professor's example.

**Recipe stuff:**
- Add new recipes. You put in the name, pick a category, write the steps, and choose ingredients.
- Edit recipes if you made a mistake. Or if you want to change something.
- Delete recipes you don't need anymore
- Search for stuff. You can type in the name or ingredient or whatever.
- Count calories. It adds up all the calories from the ingredients. That's pretty cool.

**Ingredients:**
- Add ingredients with their calories and category
- Edit them if you need to fix something
- Delete ones you dont use
- Search by name or category. You can also search by a calorie range. That took me a while to figure out.

**Meal planning:**
- You can assign recipes to different days. Like Monday, Tuesday etc.
- View what you planned for a specific day
- Delete meals from the plan

## How I built it

I used CSV files for the recipes and ingredients. Those are easy to work with. I used JSON files for the users and meal plan stuff. All the data is in a folder called "data".

When you run the program it loads everything from the files first. Then it makes you login. Then it shows you the menu. Pretty straightforward.

I split the code into different files. This makes it way easier to find stuff:
- main.py has the login and main menu
- recipes.py has all the recipe functions
- ingredients.py has the ingredient stuff  
- meals.py has the meal planning
- file_utils.py has the helper functions. It reads and writes files. My TA suggested this.

## Design decisions I made

I used dictionaries for storing recipe and ingredient data. That's what we learned in class. It works well. Each recipe has a list of ingredient IDs. That's how they're connected.

I added category validation. You can only pick from existing categories. That way you don't end up with "dinner" and "Dinner" and "DINNER" as separate categories lol. Same thing with calories. It checks that you actually enter a number.

One thing I'm proud of is the "back" option. I added it to everything. So if you start adding a recipe but change your mind you can just type "back". You're not stuck. That was my own idea.

The program saves to the files immediately. It does this whenever you change something. So you don't lose data if it crashes or whatever.

## File organization

```
recipes_project/
  main/
    main.py - login and main menu
    recipes.py - all recipe functions and menu
    ingredients.py - ingredient functions and menu
    meals.py - meal plan functions and menu
    file_utils.py - file reading/writing helpers
  data/
    recipes.csv - recipe data
    ingredients.csv - ingredient data
    users.json - usernames and passwords
    meal_plan.json - meal plans by day
    last_ids.json - tracks the last ID number used
```