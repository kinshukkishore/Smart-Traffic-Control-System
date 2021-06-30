from tc import start, stop, tc_thread
from map import add_intersection
import time
import pytest


@pytest.fixture(scope='module')
def load_example_intersection(example_intersection):
    add_intersection(example_intersection)
