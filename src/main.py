import generating
import zadanie

   
def main():
    cars = generating.create_vehicles(generating.read_file("configs/testing_config.txt"))
    print(cars)
    
    traffic = zadanie.Traffic()
    for car in cars:
            traffic.add_vehicle(car)
            print(car.color)
    print(traffic.road)

    print("Testing:")
    
    
    print("{} car {} moves to the up: ".format(cars[4].color.name, 1), traffic.down(cars[4], 1))
    for index, car in enumerate(cars):
        print(index+1)
        for i in range(1,5):
            if car.direction == zadanie.Direction.horizontal:
                print("{} car {} moves to the right: ".format(car.color.name, i), traffic.right(car, i))
                print("{} car {} moves to the left: ".format(car.color.name, i),traffic.left(car, i))
            if car.direction == zadanie.Direction.vertical:
                print("{} car {} moves to the up: ".format(car.color.name, i), traffic.up(car, i))
                print("{} car {} moves to the down: ".format(car.color.name, i), traffic.down(car, i))

            
    
if __name__ == "__main__":
    main()


