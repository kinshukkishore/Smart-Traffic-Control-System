from sympy.geometry import Point2D, Line2D
import json
from typing import Any
from map.traffic import TrafficLight
from map.road import Lane, LaneEnd, Intersection
from vehicle import Vehicle


class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if o is None:
            return None
        else:
            super().default(o)


class Point2DJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, Point2D):
            return {'x': float(o.x), 'y': float(o.y)}
        else:
            JSONEncoder.default(self, o)


class Line2DJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, Line2D):
            return {'p1': Point2DJSONEncoder().default(o.p1), 'p2': Point2DJSONEncoder().default(o.p2)}
        else:
            super().default(o)


class TrafficLightJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, TrafficLight):
            return {'id': o.id, 'signal': o.signal.name}
        else:
            super().default(o)


class LaneEndJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, LaneEnd):
            return {'id': o.id,
                    'boundary': Line2DJSONEncoder().default(o.boundary),
                    'trafficLight': TrafficLightJSONEncoder().default(o.traffic_light)}
        else:
            super().default(o)


class LaneJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, Lane):
            return {'id': o.id,
                    'side1': Line2DJSONEncoder().default(o.side1),
                    'side2': Line2DJSONEncoder().default(o.side2)}
        else:
            super().default(o)


class IntersectionJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, Intersection):
            return {'id': o.id,
                    'lanes': [LaneJSONEncoder().default(end.lane) for end in [*o.incoming_ends, *o.outgoing_ends]],
                    'laneEnds': [LaneEndJSONEncoder().default(end) for end in [*o.incoming_ends, *o.outgoing_ends]]}
        else:
            super().default(o)


class VehicleJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, Vehicle):
            return {'id': o.id, 'p': Point2DJSONEncoder().default(o.p)}
        else:
            super().default(o)