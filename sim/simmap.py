# simulation map
from map.road import Lane, LaneEnd, Intersection
from map.road import TrafficLight, TrafficSignal
from sympy.geometry import Line2D, Point2D


# meters
lw = 10
rw = lw * 2  # meters
rl = 50  # meters

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

x121 = x1 + lw / 3
x122 = x121 + lw / 3
x231 = x2 + lw / 3
x232 = x231 + lw / 3

y121 = y1 + lw / 3
y122 = y121 + lw / 3
y231 = y2 + lw / 3
y232 = y231 + lw / 3


def path121(d):
    d1 = y121 - y0
    if d <= d1:
        return Point2D(x232, y0 + d)
    else:
        return Point2D(x232 + (d - d1), y121)


def path122(d):
    d1 = y122 - y0
    if d <= d1:
        return Point2D(x231, y0 + d)
    else:
        return Point2D(x231 + (d - d1), y122)


def path131(d):
    return Point2D(x232, y0 + d)


def path132(d):
    return Point2D(x231, y0 + d)


def path141(d):
    d1 = y232 - y0
    if d <= d1:
        return Point2D(x232, y0 + d)
    else:
        return Point2D(x232 - (d - d1), y232)


def path142(d):
    d1 = y231 - y0
    if d <= d1:
        return Point2D(x231, y0 + d)
    else:
        return Point2D(x231 - (d - d1), y231)


def path231(d):
    d1 = x4 - x232
    if d <= d1:
        return Point2D(x4 - d, y232)
    else:
        return Point2D(x232, y232 + (d - d1))


def path232(d):
    d1 = x4 - x231
    if d <= d1:
        return Point2D(x4 - d, y231)
    else:
        return Point2D(x231, y231 + (d - d1))


def path241(d):
    return Point2D(x4 - d, y232)


def path242(d):
    return Point2D(x4 - d, y231)


def path211(d):
    d1 = x4 - x121
    if d <= d1:
        return Point2D(x4 - d, y232)
    else:
        return Point2D(x121, y232 - (d - d1))


def path212(d):
    d1 = x4 - x122
    if d <= d1:
        return Point2D(x4 - d, y231)
    else:
        return Point2D(x122, y231 - (d - d1))


def path341(d):
    d1 = y4 - y232
    if d <= d1:
        return Point2D(x121, y4 - d)
    else:
        return Point2D(x121 - (d - d1), y232)


def path342(d):
    d1 = y4 - y231
    if d <= d1:
        return Point2D(x122, y4 - d)
    else:
        return Point2D(x122 - (d - d1), y231)


def path311(d):
    return Point2D(x121, y4 - d)


def path312(d):
    return Point2D(x122, y4 - d)


def path321(d):
    d1 = y4 - y121
    if d <= d1:
        return Point2D(x121, y4 - d)
    else:
        return Point2D(x121 + (d - d1), y121)


def path322(d):
    d1 = y4 - y122
    if d <= d1:
        return Point2D(x122, y4 - d)
    else:
        return Point2D(x122 + (d - d1), y122)


def path411(d):
    d1 = x121 - x0
    if d <= d1:
        return Point2D(x0 + d, y121)
    else:
        return Point2D(x121, y121 - (d - d1))


def path412(d):
    d1 = x122 - x0
    if d <= d1:
        return Point2D(x0 + d, y122)
    else:
        return Point2D(x122, y122 - (d - d1))


def path421(d):
    return Point2D(x0 + d, y121)


def path422(d):
    return Point2D(x0 + d, y122)


def path431(d):
    d1 = x232 - x0
    if d <= d1:
        return Point2D(x0 + d, y121)
    else:
        return Point2D(x232, y121 + (d - d1))


def path432(d):
    d1 = x231 - x0
    if d <= d1:
        return Point2D(x0 + d, y122)
    else:
        return Point2D(x231, y122 + (d - d1))


def __getattr__(name):
    result = globals().get(name, None)
    if result is None:
        raise AttributeError(name)
    else:
        return result


traffic_lights = [TrafficLight(TrafficSignal.STOP) for _ in range(4)]

road1_ends = [LaneEnd(Line2D(Point2D(x2, y1), Point2D(x3, y1)), traffic_lights[0]),
              LaneEnd(Line2D(Point2D(x1, y1), Point2D(x2, y1))),
              LaneEnd(Line2D(Point2D(x1, y0), Point2D(x2, y0))),
              LaneEnd(Line2D(Point2D(x2, y0), Point2D(x3, y0)))]

road2_ends = [LaneEnd(Line2D(Point2D(x3, y2), Point2D(x3, y3)), traffic_lights[1]),
              LaneEnd(Line2D(Point2D(x3, y1), Point2D(x3, y2))),
              LaneEnd(Line2D(Point2D(x4, y1), Point2D(x4, y2))),
              LaneEnd(Line2D(Point2D(x4, y2), Point2D(x4, y3)))]

road3_ends = [LaneEnd(Line2D(Point2D(x1, y3), Point2D(x2, y3)), traffic_lights[2]),
              LaneEnd(Line2D(Point2D(x2, y3), Point2D(x3, y3))),
              LaneEnd(Line2D(Point2D(x2, y4), Point2D(x3, y4))),
              LaneEnd(Line2D(Point2D(x1, y4), Point2D(x2, y4)))]

road4_ends = [LaneEnd(Line2D(Point2D(x1, y1), Point2D(x1, y2)), traffic_lights[3]),
              LaneEnd(Line2D(Point2D(x1, y2), Point2D(x1, y3))),
              LaneEnd(Line2D(Point2D(x0, y2), Point2D(x0, y3))),
              LaneEnd(Line2D(Point2D(x0, y1), Point2D(x0, y2)))]

road_ends = [road1_ends, road2_ends, road3_ends, road4_ends]
lane_ends = [[road_end[0], road_end[3]] for road_end in road_ends]
lane_ends.extend([[road_end[1], road_end[2]] for road_end in road_ends])
lanes = []
for lane_end in lane_ends:
    side1 = Line2D(lane_end[0].boundary.p1, lane_end[1].boundary.p1)
    side2 = Line2D(lane_end[0].boundary.p2, lane_end[1].boundary.p2)
    lane = Lane(*lane_end, side1=side1, side2=side2)
    lanes.append(lane)
    for end in lane_end:
        end.lane = lane
intersection = Intersection(set([road_end[0] for road_end in road_ends]), set([road_end[1] for road_end in road_ends]))
