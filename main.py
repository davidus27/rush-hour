import generating

   
def main():
    cars = generating.generate_cars()
    '''
    traffic = zadanie.Traffic()
    for car in cars:
            traffic.add_vehicle(car)
    print(traffic.road)
    '''
    #new thingy
    cars = generating.create_vehicles(generating.read_file("configs/testing_config.txt"))
    
       
if __name__ == "__main__":
    main()


