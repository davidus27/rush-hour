import zadanie

def generate_cars():
    cars = [zadanie.Vehicle(color = c, starting_position = [index,0]) for index,c in enumerate(zadanie.Color)]
    
    for car in cars:
        car.size = zadanie.Size.medium
        car.direction = zadanie.Direction.horizontal
    return cars

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
    for c in zadanie.Color:
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
        size = zadanie.Size(int(i[1]))
        cordinates = [ int(i[2]) -1 , int(i[3]) -1 ]
        direction = zadanie.Direction(i[4])
        cars.append(zadanie.Vehicle(color, size, cordinates, direction))
    return cars
    


