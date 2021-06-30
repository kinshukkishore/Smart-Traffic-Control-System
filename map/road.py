from dataclasses import dataclass, field
from sympy.geometry import Line2D, Point2D, Polygon
from map.traffic import TrafficLight, TrafficSignal
from map.util import next_road_id, next_roadend_id, next_intersection_id
from typing import Set


@dataclass
class LaneEnd:
    boundary: Line2D = field(compare=False, hash=False)
    traffic_light: TrafficLight = field(default=None, compare=False, hash=False)
    lane: 'Lane' = field(default=None, compare=False, hash=False)
    id: int = field(default_factory=next_roadend_id, compare=True, hash=True)

    @property
    def traffic_signal(self):
        if self.traffic_light is None:
            return TrafficSignal.GO
        else:
            return self.traffic_light.signal

    @traffic_signal.setter
    def traffic_signal(self, value):
        if self.traffic_light is None:
            raise AttributeError('TrafficLight is not present at this LaneEnd')
        self.traffic_light.signal = value

    def distance(self, p: Point2D):
        self.boundary.distance(p)

    def __hash__(self):
        return hash(self.id)


@dataclass(frozen=True)
class Lane:
    end1: LaneEnd = field(compare=False, hash=False)
    end2: LaneEnd = field(compare=False, hash=False)
    side1: Line2D = field(compare=False, hash=False)
    side2: Line2D = field(compare=False, hash=False)
    id: int = field(default_factory=next_road_id, compare=True, hash=True)

    def on(self, p: Point2D):
        return Polygon(*self.side1.points, *self.side2.points).encloses_point(p)

    def nearest_end(self, p: Point2D):
        return self.end1 if self.end1.distance(p) < self.end2.distance(p) else self.end2


@dataclass(frozen=True)
class Intersection:
    incoming_ends: Set[LaneEnd] = field(compare=False, hash=False)
    outgoing_ends: Set[LaneEnd] = field(compare=False, hash=False)
    id: int = field(default_factory=next_intersection_id, compare=True, hash=True)

    def traffic_lights(self):
        result = []
        for end in [*self.incoming_ends, *self.outgoing_ends]:
            if end.traffic_light is not None:
                result.append(end.traffic_light)
        return result
