import pytest
from vehicle import Vehicle, add, vehicles
from sympy.geometry import Point2D


@pytest.fixture
def example_vehicle():
    return Vehicle(Point2D(0, 0))


def test_vehicle(example_vehicle):
    assert isinstance(example_vehicle, Vehicle)


def test_add(example_vehicle):
    add(example_vehicle)
    assert example_vehicle in vehicles


def test_move_vehicle(example_vehicle):
    p = Point2D(15, 15)
    example_vehicle.p = p
    assert example_vehicle.p == p


def test_add_type_error():
    with pytest.raises(TypeError):
        add(5)
