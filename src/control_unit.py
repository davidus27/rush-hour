from enum import Enum
from copy import deepcopy 
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
    black = 9
    brown = 10
    gold = 11
    indigo = 12
    silver = 13



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
        """
        Returns all positional cordinates of car
        """
        positions = []
        for i in range(self.size.value):
            y = self.starting_position[0]
            x = self.starting_position[1]
            if x < 0 or y < 0 or x >= 6 or y >= 6:
                return None
            if self.direction == Direction.vertical:
                if y + i > 6:
                    return None
                positions.append((y+i,x))
            if self.direction == Direction.horizontal:
                if x + i > 6:
                    return None
                positions.append((y,x+i))
        return positions 
   

class Traffic(object):
    def __init__(self, vehicles = [], height = 6, width = 6):
        self.vehicles = vehicles
        self.road = zeros((width, height))
        self.path = []
        self.width = width
        self.height = height
    
    def get_operations(self):
        """
        Prints out all operations
        """
        for path in self.path:
            print("{}({}, {})".format(path[0], path[1],path[2]))

    def add_vehicle(self, vehicle):
        """
        Adds vehicle to the roadmap
        """
        positions = vehicle.position
        if positions is None:
            return None
        for pos in positions:
            y = pos[0] 
            x = pos[1]
            self.road[y][x] = vehicle.color.value
        return self 

    def remove_vehicle(self, vehicle):
        """
        Removes vehicle from the roadmap
        """
        positions = vehicle.position
        if positions is None:
            return None
        for pos in positions:
            y = pos[0]
            x = pos[1]
            self.road[y][x] = 0
        return self


def check_right(traffic, vehicle, length):
    """
    Control if vehicle can move to the right
    """
    if vehicle.direction is Direction.vertical:
        return False
    for index in range(1,length + 1):
        y = vehicle.starting_position[0]
        x = vehicle.starting_position[1] 
        offset = x + vehicle.size.value - 1
        if offset + index > traffic.width-1:
            return False
        if traffic.road[y][offset+index] != 0:
            return False
    return True


def right(traffic, vehicle, length):
    """
    Operation to move vehicle right
    """
    new = deepcopy(traffic)
    new.remove_vehicle(vehicle)
    index = traffic.vehicles.index(vehicle)
    new.vehicles[index].starting_position[1] += length
    new.add_vehicle(new.vehicles[index])
    return new

def check_left(traffic, vehicle, length):
    """
    Control if vehicle can move to the left
    """
    if vehicle.direction is Direction.vertical:
        return False
    for index in range(1,length + 1): 
        y = vehicle.starting_position[0]
        x = vehicle.starting_position[1] 
        if x - index < 0:
            return False
        if traffic.road[y][x-index] != 0:
            return False
    return True

def left(traffic, vehicle, length):
    """
    Operation to move vehicle left
    """
    new = deepcopy(traffic)
    new.remove_vehicle(vehicle)
    index = traffic.vehicles.index(vehicle)
    new.vehicles[index].starting_position[1] -= length
    new.add_vehicle(new.vehicles[index])
    return new

def check_up(traffic, vehicle, length):
    """
    Control if vehicle can move up
    """
    if vehicle.direction is Direction.horizontal:
        return False 
    for index in range(1, length + 1): 
        y = vehicle.starting_position[0]
        x = vehicle.starting_position[1] 
        if y - index < 0:
            return False
        if traffic.road[y-index][x] != 0:
            return False
    return True

def up(traffic, vehicle, length):
    """
    Operation to move vehicle up
    """
    new = deepcopy(traffic)
    new.remove_vehicle(vehicle)
    index = traffic.vehicles.index(vehicle)
    new.vehicles[index].starting_position[0] -= length
    new.add_vehicle(new.vehicles[index])
    return new

def check_down(traffic, vehicle, length):
    """
    Control if vehicle can move down
    """
    if vehicle.direction is Direction.horizontal:
        return False
    for index in range(1, length + 1): 
        y = vehicle.starting_position[0]
        x = vehicle.starting_position[1] 
        offset = y + vehicle.size.value - 1
        if offset + index > traffic.height-1:
            return False
        if traffic.road[offset+index][x] != 0:
            return False
    return True

def down(traffic, vehicle, length):
    """
    Moving vehicle down in new copy of traffic
    """
    new = deepcopy(traffic) #making new copy of object
    new.remove_vehicle(vehicle) #removing vehicle from roadmap
    index = traffic.vehicles.index(vehicle)
    new.vehicles[index].starting_position[0] += length #moving position of the vehicle
    new.add_vehicle(new.vehicles[index]) #adding changed vehicle to the traffic
    return new


def is_goal(traffic):
    """
    Finding goal state
    """
    if traffic.road[2][5] == Color.red.value and traffic.road[2][4] == Color.red.value:
        return True
    return False
