import control_unit


class IterativeDeepening(object):
    def __init__(self, traffic, vehicles):
        self.traffic = traffic
        self.vehicles = vehicles    #red vehicle needs to be first
        self.path = [] #storing actual path from root
        
    def _find_red(self):
        for index, vehicle in enumerate(self.vehicles):
            if vehicle.color == control_unit.Color.red:
                return index
        return None

    def iddfs(self, root):
        red_position = self._find_red()
        #escaped = control_unit.is_goal(self.vehicles[red_position])
        depth = 0
        while True:
            found, remaining = self.dls(root, depth)
            if found:
                return found
            elif not remaining:
                return None
            depth += 1
            #just testing
            if depth > 3:
                return

    def _unpack(self):
        """
        Returns list of operations that can be used in traffic
        """
        operations = []
        for vehicle in self.vehicles:
            if vehicle.direction == control_unit.Direction.horizontal:
               operations.append(self.traffic.right)
               operations.append(self.traffic.left)
            else:
               operations.append(self.traffic.up)
               operations.append(self.traffic.down)
        return operations
                
    def dls(self, node, depth):
        if depth == 0:
            if control_unit.is_goal(node): 
                return node, True
            else:
                return None, True
        elif depth > 0:
            any_remaining = False
            for child in node:
                found, remaining = self.dls(child, depth-1)
                if found:
                    return found,True
                if remaining:
                    any_remaining = True
            return None, any_remaining