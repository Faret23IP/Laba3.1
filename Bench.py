from FabricMaterial import FabricMaterial


class Bench:
    def __init__(self, fabric_material: FabricMaterial,
                 model: str = "",
                 weight: float = 0,
                 fabric_width: float = 0,
                 fabric_area: float = 0,
                 power: float = 0):
        self.model = model
        self.fabric_material = fabric_material
        self.weight = weight
        self.fabric_width = fabric_width
        self.fabric_area = fabric_area
        self.power = power

    @property
    def get_info(self):
        return f"model: {self.model} \n" \
               f"fabric material: {self.fabric_material} \n" \
               f"weight: {self.weight} \n" \
               f"fabric width: {self.fabric_width} \n" \
               f"fabric area: {self.fabric_area} \n" \
               f"power: {self.power} \n"
