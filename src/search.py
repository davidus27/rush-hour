import control_unit


class IterativeDeepening(object):
    def __init__(self, traffic, vehicles):
        self.traffic = traffic
        self.vehicles = vehicles    #red vehicle needs to be first
        self.path = [] #storing actual path from root
        self.depth = 0
        
    def _find_red(self):
        for index, vehicle in enumerate(self.vehicles):
            if vehicle.color == control_unit.Color.red:
                return index
        return None

    def iddfs(self, root):
        red_position = _find_red()
        remaining = 0
        escaped = control_unit.found_end(self.vehicles[red_position])
        if escaped:
            return escaped #vehicle escaped
        elif remaining:
            return None #searched everything

    
    def dls(self, node, depth):
        pass


    
    

