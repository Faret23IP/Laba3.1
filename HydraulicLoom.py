from Bench import Bench
from FabricMaterial import FabricMaterial


class HydraulicLoom(Bench):
    def __init__(self, fabric_material: FabricMaterial,
                 model: str = "",
                 weight: float = 0,
                 fabric_width: float = 0,
                 fabric_area: float = 0,
                 power: float = 0,
                 lubrication_system: str = "",
                 air_supply: str = "",
                 edge_forming_mechanism: str = ""):
        super().__init__(fabric_material, model, weight, fabric_width, fabric_area, power)
        self.lubrication_system = lubrication_system
        self.air_supply = air_supply
        self.edge_forming_mechanism = edge_forming_mechanism

    def get_info(self):
        return f"model: {self.model} \n" \
               f"fabric material: {self.fabric_material} \n" \
               f"weight: {self.weight} \n" \
               f"fabric width: {self.fabric_width} \n" \
               f"fabric area: {self.fabric_area} \n" \
               f"power: {self.power} \n" \
               f"lubrication system: {self.lubrication_system} \n" \
               f"air supply: {self.air_supply} \n" \
               f"edge forming mechanism: {self.edge_forming_mechanism} \n"
