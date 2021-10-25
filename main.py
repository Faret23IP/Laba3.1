from LoomManager import LoomManager
from Bench import Bench
from HydraulicLoom import HydraulicLoom
from PneumaticLoom import PneumaticLoom
from FabricMaterial import FabricMaterial
from StopType import StopType


def main1():
    bench = Bench(fabric_material=FabricMaterial.SILK, model="model_001", weight=120, fabric_width=2, fabric_area=4,
                  power=1200)

    hydraulicloom = HydraulicLoom(fabric_material=FabricMaterial.WOOL, model="model_002", weight=220, fabric_width=4,
                                  fabric_area=16,
                                  power=1200, lubrication_system="+1", air_supply="+2", edge_forming_mechanism="+3")

    pneumaticloom = PneumaticLoom(fabric_material=FabricMaterial.LINEN, stop_type=StopType.AUTOMATIC, model="model_003",
                                  weight=200,
                                  fabric_width=3,
                                  fabric_area=9, number_of_revolutions_ps=4, flange_diameter=3)

    benches = LoomManager([bench, hydraulicloom, pneumaticloom])

    print('Sorted by fabric area:\n' + str(benches.sort_by_fabric_area([bench, hydraulicloom, pneumaticloom])) + '\n')
    print('Sorted by power:\n' + str(benches.sort_by_power([bench, hydraulicloom, pneumaticloom], True)) + '\n')
    print('Searching the object by fabric material: ' + str(
        benches.search_by_fabric_material(fabric_material=FabricMaterial.WOOL)) + '\n')


if __name__ == '__main__':
    main1()