shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor",
    "chusteczki",
    "papier toaletowy",
    ]

def shopping(items):
    shopping_cart = "W koszyku znajdują się:\n"
    for item in items:
        shopping_cart += f"- {item}\n"
    return shopping_cart

basket = shopping(shopping_items)
print(basket)
# ojej 