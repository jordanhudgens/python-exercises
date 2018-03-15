import secrets

menu = {
  'appetizers': ['Chips', 'Quesadillas', 'Flatbread'],
  'entrees': ['Steak', 'Chicken', 'Lobster'],
  'dessers': ['Cheesecake', 'Cake', 'Cupcake']
}

def daily_special(menu_dictionary):
  menu_items = []

  for _, category_items in menu_dictionary.items():
    menu_items.extend(category_items)

  return secrets.choice(menu_items)


print(daily_special(menu))

