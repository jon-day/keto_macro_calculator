"""
The typical macro ratio for keto looks like the following:

    5% of calories coming from carbs
    25% of calories coming from protein
    70% of calories coming from fat

    This script assumes you are using the 4-4-9 method which is not the most precise but still a good indicator
    of how you are doing. Essentially it is the net carbs * 4, protein * 4, and fat * 9

    I also convert everything to ounces because USA #1
    Food macros from https://www.nutritionix.com
"""


class Food:
    def __init__(self, name, fat, protein, total_carbohydrates, dietary_fiber, units, unit_measurement):
        # Assume that everything but the units are in grams
        self.name = name
        self.fat = fat * 9
        self.protein = protein * 4
        self.total_carbohydrates = total_carbohydrates
        self.dietary_fiber = dietary_fiber
        self.net_carbohydrates = (total_carbohydrates - dietary_fiber) * 4
        if unit_measurement == 'gram':
            self.units = units * 0.035274
        elif unit_measurement == 'cup':
            self.units = units / 8
        elif unit_measurement == 'liter':
            self.units = units / 33.814
        elif unit_measurement == 'tablespoon':
            self.units == units * .5
        else:
            self.units = units
        self.unit_measurement = unit_measurement
        self.calories = self.fat + self.protein + self.net_carbohydrates

    def calculate_ratios(self):
        print(f"""Calories: {self.calories} | Fiber {self.dietary_fiber}
Fat / Protein / Net Carb ratios:
{round(self.fat/self.calories, 2)} / {round(self.protein/self.calories, 2)} / {round(self.net_carbohydrates/self.calories, 2)}""")

def calculate_meal_macros(*ingredients):
    # takes in tuples of foods and how many ounces you are eating of it
    calories = 0
    fat = 0
    protein = 0
    fiber = 0
    net_carbs = 0
    for ingredient in ingredients:
        ratio = ingredient[1] / ingredient[0].units
        calories += ingredient[0].calories * ratio
        fat += ingredient[0].fat * ratio
        protein += ingredient[0].protein * ratio
        fiber += ingredient[0].dietary_fiber * ratio
        net_carbs += ingredient[0].net_carbohydrates * ratio
    fat_ratio = round(fat/calories, 2)
    protein_ratio = round(protein/calories, 2)
    net_carb_ratio = round(net_carbs/calories, 2)
    print(f"Calories: {round(calories, 2)} | Fiber {round(fiber, 2)}")
    print("Fat / Protein / Net Carb ratios:")
    print(f"{fat_ratio} / {protein_ratio} / {net_carb_ratio}")


avocado = Food("avocado",
          fat=29,
          protein=4,
          total_carbohydrates=17,
          dietary_fiber=13,
          units=201,
          unit_measurement='gram',
)

bacon = Food(
    name="bacon",
    fat=12,
    protein=12,
    total_carbohydrates=.6,
    dietary_fiber=0,
    units=35,
    unit_measurement='gram',
)

large_egg = Food(
    name="egg",
    fat=4.8,
    protein=6.3,
    total_carbohydrates=.4,
    dietary_fiber=0,
    units=50,
    unit_measurement='gram',
)

almonds = Food(
    name="almonds",
    fat=.7,
    protein=.3,
    total_carbohydrates=.3,
    dietary_fiber=.1,
    units=1.3,
    unit_measurement='gram',
)

brocolus = Food(
    name="brocolus",
    fat=.1,
    protein=.9,
    total_carbohydrates=2.7,
    dietary_fiber=1.2,
    units=37,
    unit_measurement='gram',
)

chicken_breast = Food(
    name="chicken_breast",
    fat=4.3,
    protein=37,
    total_carbohydrates=0,
    dietary_fiber=0,
    units=120,
    unit_measurement='gram',
)

cauliflower = Food(
    name="cauliflower",
    fat=2.6,
    protein=11,
    total_carbohydrates=24,
    dietary_fiber=13,
    units=575,
    unit_measurement='gram',
)
calculate_meal_macros(
    (avocado, 6),
    (bacon, 3),
    (large_egg, 1),
    (almonds, 4),
    (chicken_breast, 5),
    (cauliflower, 4),
    (brocolus, 4),
)
