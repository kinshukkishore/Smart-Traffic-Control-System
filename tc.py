# traffic control
from map.traffic import TrafficSignal
from vehicle import vehicles
from datetime import timedelta
import time
from map import intersections
from threading import Thread
import sys


MAX_FLOW_TIME = timedelta(seconds=30)
SLOW_DOWN_TIME = timedelta(seconds=5)
FLOW_TIME_PER_VEHICLE = timedelta(seconds=3)


class TrafficControl:
    def __init__(self, intersection):
        self.intersection = intersection
        self.max_block_time = MAX_FLOW_TIME * len(intersection.incoming_ends)
        self.blocked_lane_ends = {}  # {lane_end: timedelta(seconds=time.time()}
        self.last_flow_update = timedelta(seconds=0)
        self.flow_lane = None

    def vehicle_count(self):
        vc = {lane_end: 0 for lane_end in self.intersection.incoming_ends}
        for vehicle in list(vehicles):
            for lane_end in self.intersection.incoming_ends:
                if lane_end.lane.on(vehicle.p):
                    vc[lane_end] += 1
                    break

        return vc

    def update(self):
        vc = self.vehicle_count()
        packed_lane_end = None
        empty_lane_end = None
        max_vc = -1
        min_vc = sys.maxsize
        for lane_end, count in vc.items():
            if count > max_vc:
                packed_lane_end = lane_end
                max_vc = count
            if count < min_vc:
                empty_lane_end = lane_end
                min_vc = count

        if min_vc < 5 and empty_lane_end.traffic_signal == self.flow_lane:
            empty_lane_end.traffic_signal = TrafficSignal.SLOW_DOWN
            packed_lane_end.traffic_signal = TrafficSignal.READY
            time.sleep(SLOW_DOWN_TIME.seconds)
            empty_lane_end.traffic_signal = TrafficSignal.STOP
            packed_lane_end.traffic_signal = TrafficSignal.GO
            self.flow_lane = packed_lane_end
            self.last_flow_update = timedelta(seconds=time.time())
            return

        if packed_lane_end.traffic_signal not in (TrafficSignal.GO, TrafficSignal.READY) \
                and timedelta(seconds=time.time()) >= self.last_flow_update + MAX_FLOW_TIME:
            if self.flow_lane is not None:
                self.flow_lane.traffic_signal = TrafficSignal.SLOW_DOWN
            packed_lane_end.traffic_signal = TrafficSignal.READY
            time.sleep(SLOW_DOWN_TIME.seconds)
            if self.flow_lane is not None:
                self.flow_lane.traffic_signal = TrafficSignal.STOP
            packed_lane_end.traffic_signal = TrafficSignal.GO
            self.flow_lane = packed_lane_end


traffic_controls = []
TRAFFIC_UPDATE_DELAY = timedelta(milliseconds=100)
_stop_traffic_control = False


def setup():
    global traffic_controls
    traffic_controls = [TrafficControl(intersection) for intersection in intersections]


def update():
    for traffic_control in traffic_controls:
        traffic_control.update()


def traffic_operation():
    while not _stop_traffic_control:
        update()
        time.sleep(0.1)


tc_thread = Thread(target=traffic_operation, daemon=True)


def start():
    tc_thread.start()


def stop():
    global _stop_traffic_control
    _stop_traffic_control = True


def traffic_lights():
    result = []
    for traffic_control in traffic_controls:
        for end in traffic_control.intersection.incoming_ends:
            if end.traffic_light is not None:
                result.append(end.traffic_light)
    return result
