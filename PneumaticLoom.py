from FabricMaterial import FabricMaterial
from Bench import Bench
from StopType import StopType


class PneumaticLoom(Bench):
    def __init__(self, fabric_material: FabricMaterial,
                 stop_type: StopType,
                 model: str = "",
                 weight: float = 0,
                 fabric_width: float = 0,
                 fabric_area: float = 0,
                 power: float = 0,
                 number_of_revolutions_ps: float = 0,
                 flange_diameter: float = 0):
        super().__init__(fabric_material, model, weight, fabric_width, fabric_area, power)
        self.number_of_revolutions_ps = number_of_revolutions_ps
        self.flange_diameter = flange_diameter
        self.stop_type = stop_type

    def get_info(self):
        return f"model: {self.model} \n" \
               f"fabric material: {self.fabric_material} \n" \
               f"stop type: {self.stop_type} \n" \
               f"weight: {self.weight} \n" \
               f"fabric width: {self.fabric_width} \n" \
               f"fabric area: {self.fabric_area} \n" \
               f"power: {self.power} \n" \
               f"number_of_revolutions_ps: {self.number_of_revolutions_ps} \n" \
               f"flange_diameter: {self.flange_diameter} \n"
