import generating
import search
   
def main():
    cars = generating.create_vehicles(generating.read_file("configs/testing_config.txt"))
    traffic = generating.generate_cars(cars)
    
    algo = search.IterativeDeepening(traffic, cars)

    print(traffic.road)
    print(algo.dfs(traffic, 2))
    
    
    
    """
    print("Testing:")
    print("{} car {} moves to the right: ".format(cars[1].color.name, 1), traffic.right(cars[1],1))
    print("{} car {} moves to the right: ".format(cars[2].color.name, 1), traffic.up(cars[2],1))
    print("{} car {} moves to the right: ".format(cars[3].color.name, 1), traffic.up(cars[3],1))
    print("{} car {} moves to the right: ".format(cars[6].color.name, 3), traffic.left(cars[6],3))

    print("{} car {} moves to the right: ".format(cars[5].color.name, 2), traffic.left(cars[5],2))
    print("{} car {} moves to the right: ".format(cars[7].color.name, 3), traffic.down(cars[7],3))
    print("{} car {} moves to the right: ".format(cars[4].color.name, 2), traffic.down(cars[4],2))
    print("{} car {} moves to the right: ".format(cars[0].color.name, 3), traffic.right(cars[0],3))
    
    print(traffic.road)
    """
    
if __name__ == "__main__":
    main()


