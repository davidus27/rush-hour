from enum import Enum
from numpy import zeros


class Color(Enum):
    none = 0
    red = 1
    orange = 2
    yellow = 3
    purple = 4
    gray = 5
    blue = 6
    green = 7

class Size(Enum):
    small = 2
    medium = 3


class Direction(Enum):
    horizontal = "h"
    vertical = "v"



class Vehicle(object):
    def __init__(self, color, starting_position, size, direction):
        self.color = color
        self.starting_position = starting_postion
        self.size = size
        self.direction = direction
        self.postion = self.get_position()

    def get_postion(self):
            

class Traffic(object):
    def __init__(self):
        self.road = zeros((6,6))

    def add_vehicle(self, vehicle):
        pass         






