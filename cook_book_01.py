def read_recipes(file_path, desired_dishes):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cook_book = {}
    i = 0
    while i < len(lines):

        dish_name = lines[i].strip()
        i += 1
        
        num_of_ingredients = int(lines[i].strip())
        i += 1
        
        ingredients = []
        for _ in range(num_of_ingredients):
            ingredient_line = lines[i].strip().split(' | ')
            ingredient_name, quantity, measure = ingredient_line
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
            i += 1
      
        if dish_name in desired_dishes:
            cook_book[dish_name] = ingredients
        i += 1  

    return cook_book

file_path = 'recipes.txt'  
desired_dishes = {"Запеченный картофель", "Утка по-пекински", "Омлет"}
cook_book = read_recipes(file_path, desired_dishes)
print(cook_book)
