fruit = input("Item: ").lower().strip()

calories = {
    "apple": 130,
    "banana":110,
    "sweet cherries":100,
    "kiwifruit":90,
    "orange":80,
    "peach":60,
    "strawberries":50,
    "pear":100,
    "lime":20,
    "watermelon":80,
    "avocado":50,
    "tangerine":50,
    "plums":70,
    "honeydew melon":50,
    "grapes":90,
    "cantaloupe":50,
}

if fruit in calories:
    print("Calories:", calories[fruit])
