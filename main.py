import zadanie

def generate_cars():
    cars = [zadanie.Vehicle(color = zadanie.Color(i), starting_position = [i,0]) for i in range(6)]
    
    for index,car in enumerate(cars):
        car.size = zadanie.Size.medium
        car.direction = zadanie.Direction.horizontal
    return cars

def main():
    
    cars = generate_cars()
    traffic = zadanie.Traffic()
    for car in cars:
            traffic.add_vehicle(car)
    print(traffic.road)


        
if __name__ == "__main__":
    main()

