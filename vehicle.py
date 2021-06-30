from dataclasses import dataclass, field
from sympy.geometry import Point2D
from typing import Dict


_last_vehicle_id = -1
vehicles = set()


def next_vehicle_id():
    global _last_vehicle_id
    _last_vehicle_id += 1
    return _last_vehicle_id


@dataclass
class Vehicle:
    p: Point2D = field(compare=False, hash=False)
    info: Dict = field(default_factory=lambda: {}, compare=False, hash=False)
    id: int = field(default_factory=next_vehicle_id, compare=True, hash=True)

    def __hash__(self):
        return hash(self.id)


def add(vehicle):
    if isinstance(vehicle, Vehicle):
        vehicles.add(vehicle)
    else:
        raise TypeError(f'Expected type {Vehicle} found {type(vehicle)}')
