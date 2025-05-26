inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]
# 1. calculate the TotalRevenue
# totalrevenue = sum(price per unit * quantity) 

total_revenue = sum(item[2] * item[3] for item in inventory)
print(total_revenue)

# 2.List low stock item if stock is less than 5 

low_stock = [item[0] for item in inventory if item[4] < 5]
print(low_stock)

# 3.calculate category wise revenue

category_revenue = {}

for item in inventory:
    name = item[0]
    category = item[1]
    unit_price = item[2]
    units_sold = item[3]

    revenue = unit_price * units_sold

    if category in category_revenue:
        category_revenue[category] += revenue
    else:
        category_revenue[category] = revenue

print("Category-wise Revenue:")
for category, revenue in category_revenue.items():
    print(f"  {category}: ${round(revenue, 2)}")