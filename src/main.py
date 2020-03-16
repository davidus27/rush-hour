import generating
import zadanie

   
def main():
    cars = generating.create_vehicles(generating.read_file("../configs/testing_config.txt"))
    print(cars)

    traffic = zadanie.Traffic()
    for car in cars:
            traffic.add_vehicle(car)
    print(traffic.road)
    
       
if __name__ == "__main__":
    main()


