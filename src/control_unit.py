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
    def __init__(self, color = Color.none, size = Size.medium, starting_position = [0,0], direction = Direction.vertical):
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
        return positions 
   

class Traffic(object):
    def __init__(self, height = 6, width = 6):
        self.road = zeros((width, height))
        self.width = width
        self.height = height

    def add_vehicle(self, vehicle):
        positions = vehicle.position
        if positions is None:
            return None
        for pos in positions:
            y = pos[0] 
            x = pos[1]
            self.road[x][y] = vehicle.color.value
        return self
    
    def remove_vehicle(self, vehicle):
        positions = vehicle.position
        if positions is None:
            return None
        for pos in positions:
            y = pos[0]
            x = pos[1]
            self.road[x][y] = 0
        return self

    def check_right(self, vehicle, length):
        if vehicle.direction is Direction.vertical:
            return False
        for index in range(1,length + 1): 
            y = vehicle.starting_position[0]
            x = vehicle.starting_position[1] 
            offset = x + vehicle.size.value - 1
            if offset + index > self.width-1:
                return False
            if self.road[y][offset+index] != 0:
                return False
        return True

    def right(self, vehicle, length):
        self.remove_vehicle(vehicle)
        vehicle.starting_position[1] += length
        self.add_vehicle(vehicle)
        return self

    def check_left(self, vehicle, length):
        if vehicle.direction is Direction.vertical:
            return False
        for index in range(1,length + 1): 
            y = vehicle.starting_position[0]
            x = vehicle.starting_position[1] 
            if x - index < 0:
                return False
            if self.road[y][x-index] != 0:
                return False

    def left(self, vehicle, length):
        self.remove_vehicle(vehicle)
        vehicle.starting_position[1] -= length 
        self.add_vehicle(vehicle)
        return self

    def check_up(self, vehicle, length):
        if vehicle.direction is Direction.horizontal:
            return False 
        for index in range(1, length + 1): 
            y = vehicle.starting_position[0]
            x = vehicle.starting_position[1] 
            if y - index < 0:
                return False
            if self.road[y-index][x] != 0:
                return False

    def up(self, vehicle, length):
        self.remove_vehicle(vehicle)
        vehicle.starting_position[0] -= length
        self.add_vehicle(vehicle)
        return True

    def check_down(self, vehicle, length):
        if vehicle.direction is Direction.horizontal:
            return False
        for index in range(1, length + 1): 
            y = vehicle.starting_position[0]
            x = vehicle.starting_position[1] 
            offset = y + vehicle.size.value - 1
            if offset + index > self.height-1:
                return False
            if self.road[offset+index][x] != 0:
                return False

    def down(self, vehicle, length):
        self.remove_vehicle(vehicle)
        vehicle.starting_position[0] += length
        self.add_vehicle(vehicle)
        return True


def _is_goal(car, gate_position = (5,2), correct_direction = Direction.horizontal): 
    if car.direction is correct_direction and gate_position in car.position:  
        return True
    return False

def is_goal(traffic):
    if traffic.road[5][2] == Color.red.value and traffic.road[5][1] == Color.red.value:
        return True
    return False
