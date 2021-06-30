from sim import simmap
import map
import vehicle
import random
import threading
import time
from map import traffic
from collections import OrderedDict
import policeclient


class Path:
    # traffic_distance = distance from start of path to traffic light
    def __init__(self, path, length, traffic_light, traffic_distance=simmap.rl):
        self.path = path
        self.vehicles = OrderedDict()  # {vehicle: distance from path start}
        self.length = length
        self.traffic_light = traffic_light
        self.traffic_distance = traffic_distance

    def move(self, distance):
        remove_vehicles = []
        last_v = None
        for v, vd in self.vehicles.items():
            vd += distance
            # Stop the vehicle right before traffic light
            if self.traffic_light.signal in (traffic.TrafficSignal.STOP, traffic.TrafficSignal.READY) \
                    and vd in range(self.traffic_distance - distance, self.traffic_distance + 1):
                if v.info['flag']:
                    # report traffic rule violation
                    if not v.info.get('reported', False):
                        policeclient.report(v)
                        v.info['reported'] = True
                else:
                    last_v = v
                    continue

            # Stop the vehicles form getting too close
            if last_v is not None:
                if (self.vehicles[last_v] - vd) < 5:
                    last_v = v
                    continue

            if vd > self.length:
                remove_vehicles.append(v)
            else:
                v.p = self.path(vd)
                self.vehicles[v] = vd
            last_v = v
        for v in remove_vehicles:
            try:
                del self.vehicles[v]
                vehicle.vehicles.remove(v)
            except ValueError as e:
                print(e)


paths = []


def setup():
    map.add_intersection(simmap.intersection)

    for i in range(1, 5):
        f = i + 2
        if f > 4:
            f = i - 2
        path1 = getattr(simmap, "path" + str(i) + str(f) + "1")
        path2 = getattr(simmap, "path" + str(i) + str(f) + "2")
        paths.append(Path(path1, (simmap.rl + simmap.rw) * 2, simmap.traffic_lights[i - 1]))
        paths.append(Path(path2, (simmap.rl + simmap.rw) * 2, simmap.traffic_lights[i - 1]))


def update():
    if random.randint(1, 4) == 1:
        path = random.choice(paths)
        if len(path.vehicles) < 20:
            v = vehicle.Vehicle(path.path(1))
            v.info['flag'] = random.randint(1, 4) == 1
            path.vehicles[v] = 0
            vehicle.add(v)

    for path in paths:
        path.move(2)


_stop_simulation = False


def simulation():
    while not _stop_simulation:
        update()
        time.sleep(0.1)


sim_thread = threading.Thread(target=simulation, daemon=True)


def start():
    sim_thread.start()


def stop():
    global _stop_simulation
    _stop_simulation = True
