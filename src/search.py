from control_unit import *

class IterativeDeepening(object):
    def __init__(self, traffic, vehicles):
        self.traffic = traffic
        self.path = [] #storing actual path from root
        self.visited = []
        
    def iddfs(self):
        #escaped = control_unit.is_goal(self.vehicles[red_position])
        depth = 0
        while True:
            found, remaining = self.dls(self.traffic, depth)
            if found:
                return found.road
            elif not remaining:
                return None
            depth += 1
            print(depth)
            self.visited = []

    def _actions(self,traffic, vehicle):
        if vehicle.direction == Direction.horizontal:
            return [right, left]
        else:
            return [up, down]

    def get_neighbours(self, traffic):
        operations = []
        for vehicle in traffic.vehicles:
            for index in range(1,5):
                if vehicle.direction == Direction.horizontal:
                    if check_right(traffic, vehicle, index):
                        op = right(traffic, vehicle, index)
                        hash_value = self.hash(op)
                        if hash_value not in self.visited:
                            operations.append(op)
                            self.visited.append(hash_value)

                    if check_left(traffic, vehicle, index):
                        op = left(traffic, vehicle, index)
                        hash_value = self.hash(op)
                        if hash_value not in self.visited:
                            operations.append(op)
                            self.visited.append(hash_value)
                else:
                    if check_up(traffic, vehicle, index):
                        op = up(traffic, vehicle, index)
                        hash_value = self.hash(op)
                        if hash_value not in self.visited:
                            operations.append(op)
                            self.visited.append(hash_value)

                    if check_down(traffic, vehicle, index):
                        op = down(traffic, vehicle, index)
                        hash_value = self.hash(op)
                        if hash_value not in self.visited:
                            operations.append(op)
                            self.visited.append(hash_value)
        return operations
            
    def hash(self, state):
        value = state.road.flatten()
        h = ''
        for v in value:
           h += str(v) 
        return h

    def dls(self, traffic, depth):
        if depth == 0:
            if is_goal(traffic):
                return traffic, True 
            else:
                return None, True

        any_remaining = False
        for child in self.get_neighbours(traffic):
            found, remaing = self.dls(child, depth-1)
            if is_goal(child):
                return traffic, True
            if found:
                return found, True
            if remaing:
                any_remaining = True

        return None,any_remaining 