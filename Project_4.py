from os import system
from copy import deepcopy
import numpy as np
import random
import time

class Cycle:
    def __init__(self, path, cost):
        self.path = path
        self.cost = cost

def readfile(filename):
    global cities
    global map
    with open(filename) as f:
        cities = int(f.readline())
    map = np.loadtxt(filename, dtype=int, skiprows=1)

def rand_init():
    rand_min = 1
    rand_max = cities
    length = cities - 1
    initial = random.sample(range(rand_min, rand_max), length)
    initial.insert(0, 0)
    initial.insert(cities, 0)
    return initial

def calc_cost(path):
    cost = 0
    for i in range(cities):
        cur_city = path[i]
        travel_to = path[i+1]
        cost += map[cur_city][travel_to]
    return cost

def find_best_neighbour(current):
    best_neighbour = deepcopy(current)
    for i in range(1, cities):
        for j in range(i+1, cities):
            temp = deepcopy(current)
            temp.path[i], temp.path[j] = temp.path[j], temp.path[i]
            temp.cost = calc_cost(temp.path)
            if temp.cost < best_neighbour.cost:
                best_neighbour = deepcopy(temp)
    return best_neighbour

def hill_climbing(initial):
    current = initial
    while True:
        best_neighbour = find_best_neighbour(current)
        if best_neighbour.cost >= current.cost:
            return current
        current = deepcopy(best_neighbour)

def print_answer(answer):
    print("\nPath: ", end="")
    for i in range(len(answer.path)):
        print(answer.path[i], end="")
        if (i % 10 == 0) and (i != 0): print("\n")
        if i < len(answer.path) - 1: print(" -> ", end="")
    print("\nCost: ", answer.cost)

def main():
    starting_text = "\nWhich input would you like to choose?\n1. input_1.txt - 5 cities\n2. input_2.txt - 100 cities\n\n> Enter the number: "

    while True:
        input_number = input(starting_text)
        if input_number == "1" or input_number == "2":
            break
        system("cls")   # sorry no linux master race
        print("Wrong input number, try again!\n")

    filename = "input_" + input_number + ".txt"
    readfile(filename)

    initial_path = rand_init()
    initial_cost = calc_cost(initial_path)
    initial = Cycle(initial_path, initial_cost)

    start_time = time.time()
    answer = hill_climbing(initial)
    print_answer(answer)

    print("\n--- Total elapsed time: %s seconds ---\n" % (time.time() - start_time))


if __name__ == "__main__":
    main()