import pytest
from map.road import Lane, LaneEnd, Intersection
from sympy.geometry import Line2D, Point2D
from tests.test_traffic import traffic_lights

# meters
lw = 4
rw = lw * 2  # meters
rl = 100  # meters

x0 = 0
x1 = rl
x2 = x1 + lw
x3 = x2 + lw
x4 = x3 + rl

y0 = 0
y1 = rl
y2 = y1 + lw
y3 = y2 + lw
y4 = y3 + rl


@pytest.fixture(scope='session')
def road1_ends(traffic_lights):
    return [LaneEnd(Line2D(Point2D(x2, y1), Point2D(x3, y1)), traffic_lights[0]),
            LaneEnd(Line2D(Point2D(x1, y1), Point2D(x2, y1)), traffic_lights[0]),
            LaneEnd(Line2D(Point2D(x1, y0), Point2D(x2, y0))),
            LaneEnd(Line2D(Point2D(x2, y0), Point2D(x3, y0)))]


@pytest.fixture(scope='session')
def road2_ends(traffic_lights):
    return [LaneEnd(Line2D(Point2D(x3, y2), Point2D(x3, y3)), traffic_lights[0]),
            LaneEnd(Line2D(Point2D(x3, y1), Point2D(x3, y2)), traffic_lights[0]),
            LaneEnd(Line2D(Point2D(x4, y1), Point2D(x4, y2))),
            LaneEnd(Line2D(Point2D(x4, y2), Point2D(x4, y3)))]


@pytest.fixture(scope='session')
def road3_ends(traffic_lights):
    return [LaneEnd(Line2D(Point2D(x1, y3), Point2D(x2, y3)), traffic_lights[0]),
            LaneEnd(Line2D(Point2D(x2, y3), Point2D(x3, y3)), traffic_lights[0]),
            LaneEnd(Line2D(Point2D(x2, y4), Point2D(x3, y4))),
            LaneEnd(Line2D(Point2D(x1, y4), Point2D(x2, y4)))]


@pytest.fixture(scope='session')
def road4_ends(traffic_lights):
    return [LaneEnd(Line2D(Point2D(x1, y1), Point2D(x1, y2)), traffic_lights[0]),
            LaneEnd(Line2D(Point2D(x1, y2), Point2D(x1, y3)), traffic_lights[0]),
            LaneEnd(Line2D(Point2D(x0, y2), Point2D(x0, y3))),
            LaneEnd(Line2D(Point2D(x0, y1), Point2D(x0, y2)))]


@pytest.fixture(scope='session')
def road_ends(road1_ends, road2_ends, road3_ends, road4_ends):
    return road1_ends, road2_ends, road3_ends, road4_ends


@pytest.fixture(scope='session')
def lanes(road_ends):
    lane_ends = [[road_end[0], road_end[3]] for road_end in road_ends]
    return [Lane(*lane_end, *[Line2D(*end.boundary.points) for end in lane_end])
            for lane_end in lane_ends]


@pytest.fixture(scope='session')
def example_intersection(road_ends):
    return Intersection(set([road_end[1]for road_end in road_ends]), set([road_end[0] for road_end in road_ends]))
