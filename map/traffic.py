import enum
from map.util import next_trafficlight_id


@enum.unique
class TrafficSignal(enum.Enum):
    STOP = 0
    SLOW_DOWN = 1
    GO = 2
    READY = 3


class TrafficLight:
    def __init__(self, signal=TrafficSignal.GO, id=None):
        self.signal = signal
        if id is None:
            self.id = next_trafficlight_id()
        else:
            self.id = id

    @property
    def signal(self):
        return self._signal

    @signal.setter
    def signal(self, value):
        if isinstance(value, TrafficSignal):
            self._signal = value
        else:
            raise TypeError(f'expected {TrafficSignal} found {type(value)}')
