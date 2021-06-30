from map.traffic import TrafficLight
import pytest


@pytest.fixture(scope='session')
def traffic_lights():
    return [TrafficLight() for _ in range(4)]


def test_traffic_light(traffic_lights):
    assert isinstance(traffic_lights[0], TrafficLight)
