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
    def __init__(self, color = Color.none, starting_position = (0,0), size = Size.medium, direction = Direction.vertical):
        self.color = color
        self.starting_position = starting_position
        self.size = size
        self.direction = direction

    @property
    def position(self):
        positions = []
        for i in range(self.size.value):
            y = self.starting_position[0]
            x = self.starting_position[1]
            if x < 0 or y < 0 or x + i > 6 or y +i > 6:
                return None
            if self.direction is Direction.vertical:
                positions.append((x,y+i))
            if self.direction is Direction.horizontal:
                positions.append((x+i,y))
        return positions 


class Traffic(object):
    def __init__(self):
        self.road = zeros((6,6))

    def add_vehicle(self, vehicle):
        if vehicle.position is None:
            return None
        for position in vehicle.position:
            y = position[0]
            x = position[1]
            self.road[x][y] = vehicle.color.value
        return self




