_last_road_id = -1
_last_roadend_id = -1
_last_trafficlight_id = -1
_last_intersection_id = -1


def next_road_id():
    global _last_road_id
    _last_road_id += 1
    return _last_road_id


def next_roadend_id():
    global _last_roadend_id
    _last_roadend_id += 1
    return _last_roadend_id


def next_trafficlight_id():
    global _last_trafficlight_id
    _last_trafficlight_id += 1
    return _last_trafficlight_id


def next_intersection_id():
    global _last_intersection_id
    _last_intersection_id += 1
    return _last_intersection_id


def draw_json_str(obj):
    return obj.__draw_json_str__()