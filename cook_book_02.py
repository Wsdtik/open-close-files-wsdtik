def read_recipes(file_path):
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
        
        cook_book[dish_name] = ingredients
        i += 1 

    return cook_book

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                ing_name = ing['ingredient_name']
                measure = ing['measure']
                quantity = ing['quantity'] * person_count
                if ing_name in shop_list:
                    shop_list[ing_name]['quantity'] += quantity
                else:
                    shop_list[ing_name] = {'measure': measure, 'quantity': quantity}
    return shop_list

file_path = 'recipes.txt' 
cook_book = read_recipes(file_path)

result = get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 2)
print(result)
