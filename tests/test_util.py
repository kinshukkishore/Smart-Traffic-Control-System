import util
import json
from sympy.geometry import Point2D, Line2D
from map.traffic import TrafficLight, TrafficSignal
from map.road import LaneEnd, Lane, Intersection


def test_point2djsonencoder():
    assert json.dumps(Point2D(1, 2), cls=util.Point2DJSONEncoder) == '{"x": 1.0, "y": 2.0}'


def test_line2djsonencoder():
    actual = json.dumps(Line2D(Point2D(1, 2), Point2D(3, 4)), cls=util.Line2DJSONEncoder)
    expected = '{"p1": {"x": 1.0, "y": 2.0}, "p2": {"x": 3.0, "y": 4.0}}'
    assert actual == expected


def test_trafficlightjsonencoder():
    actual = json.dumps(TrafficLight(signal=TrafficSignal.GO, id=42), cls=util.TrafficLightJSONEncoder)
    expected = '{"id": 42, "signal": "GO"}'
    assert actual == expected


def test_laneendjsonencoder():
    lane_end = LaneEnd(boundary=Line2D(Point2D(1, 2), Point2D(3, 4)),
                       traffic_light=TrafficLight(signal=TrafficSignal.STOP, id=53), id=42)
    actual = json.dumps(lane_end, cls=util.LaneEndJSONEncoder)
    expected = '{"id": 42, "boundary": {"p1": {"x": 1.0, "y": 2.0}, "p2": {"x": 3.0, "y": 4.0}}, ' \
               '"trafficLight": {"id": 53, "signal": "STOP"}}'
    assert actual == expected


def test_lanejsonencoder():
    end1 = LaneEnd(boundary=Line2D(Point2D(1, 2), Point2D(3, 4)),
                       traffic_light=TrafficLight(signal=TrafficSignal.STOP, id=42), id=52)
    end2 = LaneEnd(boundary=Line2D(Point2D(5, 6), Point2D(7, 8)),
            traffic_light=TrafficLight(signal=TrafficSignal.STOP, id=43), id=53)
    side1 = Line2D(Point2D(9, 10), Point2D(11, 12))
    side2 = Line2D(Point2D(13, 14), Point2D(15, 16))
    lane = Lane(end1=end1, end2=end2, side1=side1, side2=side2, id=62)
    actual = json.dumps(lane, cls=util.LaneJSONEncoder)
    expected = '{"id": 62, "side1": {"p1": {"x": 9.0, "y": 10.0}, "p2": {"x": 11.0, "y": 12.0}}, ' \
               '"side2": {"p1": {"x": 13.0, "y": 14.0}, "p2": {"x": 15.0, "y": 16.0}}}'


def test_intersectionjsonencoder():

    end1 = LaneEnd(boundary=Line2D(Point2D(1, 2), Point2D(3, 4)),
                   traffic_light=TrafficLight(signal=TrafficSignal.STOP, id=42), id=52)
    end2 = LaneEnd(boundary=Line2D(Point2D(5, 6), Point2D(7, 8)),
                   traffic_light=TrafficLight(signal=TrafficSignal.STOP, id=43), id=53)
    side1 = Line2D(Point2D(9, 10), Point2D(11, 12))
    side2 = Line2D(Point2D(13, 14), Point2D(15, 16))
    lane = Lane(end1=end1, end2=end2, side1=side1, side2=side2, id=62)
    end1.lane = lane
    end2.lane = lane
    intersection = Intersection(set([end1]), set([end2]), id=63)
    actual = json.dumps(intersection, cls=util.IntersectionJSONEncoder)
    expected = '{"id": 63, ' \
               '"lanes": [{"id": 62, "side1": {"p1": {"x": 9.0, "y": 10.0}, "p2": {"x": 11.0, "y": 12.0}}, ' \
                    '"side2": {"p1": {"x": 13.0, "y": 14.0}, "p2": {"x": 15.0, "y": 16.0}}}, ' \
                    '{"id": 62, "side1": {"p1": {"x": 9.0, "y": 10.0}, "p2": {"x": 11.0, "y": 12.0}}, ' \
                    '"side2": {"p1": {"x": 13.0, "y": 14.0}, "p2": {"x": 15.0, "y": 16.0}}}], ' \
               '"laneEnds": [{"id": 52, "boundary": {"p1": {"x": 1.0, "y": 2.0}, "p2": {"x": 3.0, "y": 4.0}}, ' \
                    '"trafficLight": {"id": 42, "signal": "STOP"}}, ' \
                    '{"id": 53, "boundary": {"p1": {"x": 5.0, "y": 6.0}, "p2": {"x": 7.0, "y": 8.0}}, ' \
                    '"trafficLight": {"id": 43, "signal": "STOP"}}]}'
    assert actual == expected
