from enum import Enum
from numpy import zeros


class Color(Enum):
    none = 0
    red = 1
    orange = 2
    yellow = 3
    purple = 4
    green = 5
    light_blue = 6
    gray = 7
    dark_blue = 8

class Size(Enum):
    small = 2
    medium = 3


class Direction(Enum):
    horizontal = "h"
    vertical = "v"


class Vehicle(object):
    def __init__(self, color = Color.none, size = Size.medium, starting_position = (0,0), direction = Direction.vertical):
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
            if x < 0 or y < 0:
                return None
            if self.direction is Direction.vertical:
                if y + i > 6:
                    return None
                positions.append((x,y+i))
            if self.direction is Direction.horizontal:
                if x + i >6:
                    return None
                positions.append((x+i,y))
        print("position", positions)
        return positions 


class Traffic(object):
    def __init__(self):
        self.road = zeros((6,6))

    def add_vehicle(self, vehicle):
        positions = vehicle.position
        if positions is None:
            return None
        for position in positions:
            y = position[0] 
            x = position[1]
            self.road[x][y] = vehicle.color.value
        return self




