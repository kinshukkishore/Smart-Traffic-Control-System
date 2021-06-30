from map.road import Lane, LaneEnd, Intersection


lanes = set()
intersections = set()


def add_lane(_lane):
    if isinstance(_lane, Lane):
        lanes.add(_lane)
    else:
        raise TypeError(f'Expected type {Lane} found {type(_lane)}')


def add_intersection(intersection):
    if isinstance(intersection, Intersection):
        for lane_end in [*intersection.incoming_ends, *intersection.outgoing_ends]:
            if lane_end.lane is not None:
                add_lane(lane_end.lane)
        intersections.add(intersection)
    else:
        raise TypeError(f'Expected type {Intersection} found {type(intersection)}')
