from Bench import Bench
from FabricMaterial import FabricMaterial
from typing import List


class LoomManager:
    def __init__(self, benches=list):
        self.benches = benches

    def sort_by_fabric_area(self, benches: List[Bench], reverse: bool = False):
        return sorted(benches, key=lambda s: s.fabric_area, reverse=reverse)

    def sort_by_power(self, benches: List[Bench], reverse: bool = False):
        return sorted(benches, key=lambda s: s.power, reverse=reverse)

    def search_by_fabric_material(self, fabric_material: FabricMaterial):
        return [benches for benches in self.benches if benches.fabric_material == fabric_material]
