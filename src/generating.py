import control_unit

def generate_cars(cars):
    traffic = control_unit.Traffic()
    for index, car in enumerate(cars):
            traffic.add_vehicle(car)
    return traffic

def read_file(file_name):
    try:
        f = open(file_name, "r")
        cars = []
        for line in f:
            cars.append(line.split())
        return cars
    except:
        print("Problem with file.")
        return None

def evaluate_color(str_color):
    for c in control_unit.Color:
        if c.name == str_color: 
            return c
    return None

def create_vehicles(data):
    if data is None:
        print("Error: No data available.")
        return None
    cars = []
    for i in data: 
        color = evaluate_color(i[0])
        size = control_unit.Size(int(i[1]))
        cordinates = [ int(i[2]) -1 , int(i[3]) -1 ]
        direction = control_unit.Direction(i[4])
        cars.append(control_unit.Vehicle(color, size, cordinates, direction))
    return cars
    


