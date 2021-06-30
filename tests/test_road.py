from map.road import Intersection
from map.traffic import TrafficSignal


def test_traffic_signal_change(road1_ends):
    road1_ends[0].traffic_signal = TrafficSignal.STOP
    assert road1_ends[0].traffic_signal == TrafficSignal.STOP


def test_intersection(example_intersection):
    assert isinstance(example_intersection, Intersection)
