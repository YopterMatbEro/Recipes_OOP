from pprint import pprint


def dish_recipes():
    with open('recipe.txt', 'rt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            recipe_name = line.strip()
            quantity_ingredients = int(file.readline())
            ingredients = []
            for _ in range(quantity_ingredients):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredients_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            cook_book[recipe_name] = ingredients
            file.readline()
    file.close()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for i in range(len(dish_recipes()[dish])):
            name, quantity, measure = dish_recipes()[dish][i].values()
            if name not in ingredients:
                ingredients[name] = {'measure': measure, 'quantity': int(quantity) * person_count}
            else:
                ingredients[name]['quantity'] += int(quantity) * person_count
    return ingredients


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 1), sort_dicts=False)
# pprint(dish_recipes(), sort_dicts=False)
