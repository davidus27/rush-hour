import generating
import search
import time

CONFIG_PATH = "configs/"

def main():

    while(True):
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
        else:
            print("Goal state:")
            print("Time elapsed:", end - start)
            print(goal.road)
            print("Operations:")
            goal.get_operations()
            
    
if __name__ == "__main__":
    main()


