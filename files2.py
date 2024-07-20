cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
class Dishes:
    def get_shop_list_by_dishes(self, dishes, person_count):
      self.dishes = dishes
      self.person_count = person_count
    result = {}

    for reciepe in cook_book:
        title = reciepe[0]
        items = reciepe[1]
        for i in cook_book:
            i = items[0]
            items[1]*('person_count')


        print(title)
#append({'ingredient_name': 'measure', })

   # def __str__(self):
   #    return {'dishes': "quantity" * "person_count"}

get_shop_list_by_dishes = (['Запеченный картофель', 'Омлет'], 2)

