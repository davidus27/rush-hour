import zadanie

def generate_cars():
    cars = [zadanie.Vehicle(color = zadanie.Color(i+1), starting_position = [i,0]) for i in range(7)]
    
    for car in cars:
        car.size = zadanie.Size.medium
        car.direction = zadanie.Direction.horizontal
    return cars



def read_file(file_name):
    try:
        with open(file_name):
            data = f.read()
        f.close()
        return data
    except:
        print("Problem with file.")
        return None

def create_vehicles(data):
    if data is None:
        print("Error: No data available.")
        return None
    for i in data:
        print(i)


    
def main():
    
    cars = generate_cars()
    traffic = zadanie.Traffic()
    for car in cars:
            traffic.add_vehicle(car)
    print(traffic.road)
    
    #new thingy
    #create_vehicles(read_file("file.txt"))
    with open("file.txt"):
        data = f.read()
    print(data)

        
if __name__ == "__main__":
    main()


