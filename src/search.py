from control_unit import *



class IterativeDeepening(object):
    def __init__(self, traffic, vehicles):
        self.traffic = traffic
        self.path = [] #storing actual path from root
        self.hash_table = []
        
    def iddfs(self, limit = 55):
        """
        Iterative depth first search function
        """
        depth = 0
        while True:
            found, remaining = self.dls(self.traffic, depth)
            if found:
                return found
            elif not remaining or depth >= limit:
                return None
            depth += 1
            self.hash_table = []


    def _visited(self, traffic):
        """
        Checks the hash_table if there is hash value, 
        if not it will add it
        """
        hash_value = self.hash_function(traffic)
        if hash_value not in self.hash_table:
            self.hash_table.append(hash_value)
            return True
        return False

    def get_neighbours(self, traffic):
        """
        Creates list of computed copies of roadmap
        """
        operations = []
        for vehicle in traffic.vehicles:
            for index in range(1,5):
                if vehicle.direction == Direction.horizontal:
                    if check_right(traffic, vehicle, index):
                        node = right(traffic, vehicle, index)
                        if self._visited(node):
                            operations.append(node)                 
                            node.path.append(["right", vehicle.color.name, index])

                    if check_left(traffic, vehicle, index):
                        node = left(traffic, vehicle, index)
                        if self._visited(node):
                            operations.append(node)                 
                            node.path.append(["left", vehicle.color.name, index])

                else:
                    if check_up(traffic, vehicle, index):
                        node = up(traffic, vehicle, index)
                        if self._visited(node):
                            operations.append(node)                 
                            node.path.append(["up", vehicle.color.name, index])

                    if check_down(traffic, vehicle, index):
                        node = down(traffic, vehicle, index)
                        if self._visited(node):
                            operations.append(node)                 
                            node.path.append(["down", vehicle.color.name, index])
        return operations
            
    def hash_function(self, state):
        """
        Computes hash value
        """
        value = state.road.flatten()
        h = ''
        for v in value:
           h += str(v) 
        h.replace(".","")
        return h

    def dls(self, traffic, depth):
        """
        Performs improved version of depth first search 
        """
        if depth == 0:
            if is_goal(traffic):
                return traffic, True 
            else:
                return None, True

        any_remaining = False
        for child in self.get_neighbours(traffic):
            found, remaing = self.dls(child, depth-1)
            if is_goal(child):
                return child, True
            if found:
                return found, True
            if remaing:
                any_remaining = True
        return None,any_remaining 