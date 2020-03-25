from control_unit import *

class IterativeDeepening(object):
    def __init__(self, traffic, vehicles):
        self.traffic = traffic
        self.path = [] #storing actual path from root
        
    def iddfs(self):
        #escaped = control_unit.is_goal(self.vehicles[red_position])
        depth = 0
        while True:
            found, remaining = self.dls(self.traffic, depth)
            if found:
                return found
            elif not remaining:
                return None
            depth += 1
            print(depth)
            #just testing
            if depth > 10:
                return False

    def dfs_iterative(self, depth):
        pass
   
    def _actions(self,traffic, vehicle):
        if vehicle.direction == Direction.horizontal:
            return [right, left]
        else:
            return [up, down]

    def get_neighbours(self, traffic):
        operations = [] #list of traffices
        for vehicle in traffic.vehicles:
            for index in range(1,5):
                if vehicle.direction == Direction.horizontal:
                    if check_right(traffic, vehicle, index):
                        operations.append(right(traffic, vehicle, index))

                    if check_left(traffic, vehicle, index):
                        operations.append(left(traffic, vehicle, index))
                else:
                    if check_up(traffic, vehicle, index):
                        operations.append(up(traffic, vehicle, index))

                    if check_down(traffic, vehicle, index):
                        operations.append(down(traffic, vehicle, index))
        return operations
            
    def dls(self, traffic, depth):
        if depth == 0:
            if is_goal(traffic):
                return traffic, True 
            else:
                return None, True

        any_remaining = False
        for child in self.get_neighbours(traffic):
            found, remaing = self.dls(child, depth-1)
            if found:
                return found, True
            if remaing:
                any_remaining = True

        return None,any_remaining 