import map


def test_add_lane(lanes):
    map.add_lane(lanes[0])
    assert lanes[0] in map.lanes


def test_add_intersection(example_intersection):
    map.add_intersection(example_intersection)
    assert example_intersection in map.intersections
