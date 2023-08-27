class BuildingError(Exception):
    def __str__(self):
        return f"With so much material house cannot be built!"

def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return  "enough material"
    else:
        raise BuildingError(amount_of_material)

materials = 125
check_material(materials, 300)