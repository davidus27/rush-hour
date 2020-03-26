import generating
import search
import time

CONFIG_PATH = "configs/"

def main():
    #Start of the program
    while(True):
        print("Configurations:")
        print("1: 7 vehicles, 12 operations")
        print("2: 7 vehicles, no result")
        print("3: 6 vehicles, 8 operations")
        print("4: 8 vehicles, 11 operations")
        print("5: 7 vehicles, 9 operations")
        number = input("Choose configuration[1-9]:")
        if(number == "q"):
            print("Ending")
            break
        config_file = CONFIG_PATH + "config" + number + ".txt"
        cars = generating.create_vehicles(generating.read_file(config_file))
        traffic = generating.generate_cars(cars)
        print("Initial state:")
        print(traffic.road)
        print("Finding...")
        algo = search.IterativeDeepening(traffic, cars)
        start = time.time()
        goal = algo.iddfs()
        end = time.time()
        if goal is None:
            print("This configuration doesnt have goal state.")
            print("Time elapsed:", end - start)
        else:
            print("Goal state:")
            print("Time elapsed:", end - start)
            print(goal.road)
            print("Operations[{}]:".format(len(goal.path)))
            goal.get_operations()
            
    
if __name__ == "__main__":
    main()


