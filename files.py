# cook_book = {}
# with open('cooking.txt', encoding='utf-8') as f:
#     data = f.read()
#     # print (data)
#
# with open('cooking.txt') as f:
#     lines = f.read().splitlines()
# dic = {}
# for line in lines:

with open('cooking.txt') as f:
    x = f.read().split('\n\n')
    r = [i.split('\n') for i in x]
    cook_book = {}
    for i in r:
        cook_book[i[0]] = []
        for j in i[2:]:
            xxx = j.split(' | ')
            cook_book[i[0]].append({'ingredient_name': xxx[0], 'quantity': int(xxx[1]), 'measure': xxx[2]})
print(cook_book)


# with open ('cooking.txt') as f:
# dictionary = dict.fromkeys(ingredient-name: [1], )
# print(dictionary)

# #cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ],
#   'Фахитос': [
#     {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
#     {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
#     {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
#     ]
#   #}



# #class Dishes:
#     #def get_shop_list_by_dishes(self, dishes, person_count):
#         self.dishes = dishes
#         self.person_count = person_count
#    #def __str__(self):
#    # return result 'dishes': "quantity" * 'person_count'
