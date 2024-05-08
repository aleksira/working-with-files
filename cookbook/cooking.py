from pprint import pprint


# функция для создания словаря из одного ингредиента
def ingredient(line):
    recipe_dict = {'ingredient_name': line.split(' | ')[0],
                   'quantity': line.split(' | ')[1],
                   'measure': line.split(' | ')[2]}
    return recipe_dict



def create_dict(file):
    cook_book = {}
    with open(file, encoding='utf-8') as f:
        text = f.read()
        recipes = text.split('\n\n')  # отделяем рецепты друг от друга
        for recipe in recipes:
            lines = recipe.split('\n')  # создаем список строк каждого рецепта
            cook_book[lines[0]] = []  # ключом словаря становится нулевая строка - название блюда
            for i in range(2, int(lines[1])+2):
                cook_book[lines[0]].append(ingredient(lines[i]))  # добавляем ингредиенты в словарь по ключу
    return cook_book


# функция для создания списка покупок

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = create_dict('recipes.txt')
    for dish in dishes:
        recipe = cook_book[dish]  # находим каждое блюдо в книге рецептов
        for ingr in recipe:  # затем находим каждый ингредиент
            name = ingr['ingredient_name']
            measure = ingr['measure']
            quantity = int(ingr['quantity'])
            if name not in shop_list.keys():  # проверяем, есть ли ингредиент в нашем списке
                shop_list[name] = {'measure':measure, 'quantity':quantity*person_count}
            else:
                shop_list[name]['quantity'] += quantity*person_count
    return shop_list


# проверка :)
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински', 'Овсяная каша'], 2))